import os
from typing import Any
from collections.abc import Generator
from dify_plugin import Tool
from dify_plugin.entities.tool import ToolInvokeMessage
from tools.crypto_utils import SecurityUtils


class DecryptFileSimple(Tool):
    
    def _invoke(self, parameters: dict[str, Any]) -> Generator[ToolInvokeMessage]:
        file_obj = parameters.get('file')
        key = parameters.get('key')
        
        if not file_obj:
            yield self.create_text_message("Error: File is required")
            yield self.create_json_message({'success': False, 'error': 'File is required'})
            return
        
        if not key:
            yield self.create_text_message("Error: Key is required")
            yield self.create_json_message({'success': False, 'error': 'Key is required'})
            return
        
        try:
            import tempfile
            
            temp_dir = tempfile.gettempdir()
            input_path = os.path.join(temp_dir, file_obj.filename)
            
            with open(input_path, 'wb') as f:
                f.write(file_obj.blob)
            
            file_ext = os.path.splitext(file_obj.filename)[1].lower()
            
            if file_ext == '.pdf':
                output_filename = f"decrypted_{file_obj.filename}"
                output_path = os.path.join(temp_dir, output_filename)
                success, message = SecurityUtils.decrypt_pdf(input_path, key, output_path)
            elif file_ext == '.zip':
                output_dir = os.path.join(temp_dir, f"decrypted_{os.path.splitext(file_obj.filename)[0]}")
                output_path = output_dir
                success, message = SecurityUtils.decrypt_zip(input_path, key, output_path)
                output_filename = output_dir
            elif file_ext == '.7z':
                output_dir = os.path.join(temp_dir, f"decrypted_{os.path.splitext(file_obj.filename)[0]}")
                output_path = output_dir
                success, message = SecurityUtils.decrypt_7z(input_path, key, output_path)
                output_filename = output_dir
            else:
                yield self.create_text_message(f'Error: Unsupported file type. Simple decryption only supports PDF, ZIP, and 7Z files.')
                yield self.create_json_message({'success': False, 'error': 'Unsupported file type'})
                return
            
            if success:
                if file_ext in ['.zip', '.7z']:
                    import zipfile
                    if file_ext == '.7z':
                        import py7zr
                        archive = py7zr.SevenZipFile(input_path, mode='r', password=key)
                        files = archive.getnames()
                        archive.close()
                    else:
                        archive = zipfile.ZipFile(input_path, 'r')
                        archive.setpassword(key.encode('utf-8'))
                        files = archive.namelist()
                        archive.close()
                    
                    yield self.create_text_message(f"File decrypted successfully with simple method.\n\nFile: {file_obj.filename}\nFile type: {file_ext.upper()}\nOutput directory: {output_filename}\nExtracted files: {len(files)}")
                    
                    yield self.create_json_message({
                        'success': True,
                        'filename': file_obj.filename,
                        'file_type': file_ext.upper(),
                        'output_directory': output_filename,
                        'extracted_files_count': len(files),
                        'key': key
                    })
                else:
                    file_size = os.path.getsize(output_path)
                    file_size_mb = file_size / (1024 * 1024)
                    
                    yield self.create_text_message(f"File decrypted successfully with simple method.\n\nFile: {file_obj.filename}\nDecrypted file: {output_filename}\nFile size: {file_size_mb:.2f} MB\nFile type: {file_ext.upper()}")
                    
                    yield self.create_json_message({
                        'success': True,
                        'filename': file_obj.filename,
                        'decrypted_filename': output_filename,
                        'file_size_bytes': file_size,
                        'file_size_mb': round(file_size_mb, 2),
                        'file_type': file_ext.upper(),
                        'key': key
                    })
                    
                    yield self.create_blob_message(
                        blob=open(output_path, 'rb').read(),
                        meta={
                            'filename': output_filename,
                            'mime_type': 'application/octet-stream'
                        }
                    )
            else:
                yield self.create_text_message(message)
                yield self.create_json_message({'success': False, 'error': message})
        except Exception as e:
            yield self.create_text_message(f'Error during decryption: {str(e)}')
            yield self.create_json_message({'success': False, 'error': str(e)})
