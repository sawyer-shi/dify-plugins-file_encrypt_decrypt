import os
from typing import Any
from dify_plugin import Tool
from tools.crypto_utils import SecurityUtils


class DecryptFileSimple(Tool):
    
    def _invoke(self, parameters: dict[str, Any]) -> dict[str, Any]:
        file_obj = parameters.get('file')
        key = parameters.get('key')
        
        if not file_obj:
            return {
                'text': 'Error: File is required',
                'json': {'success': False, 'error': 'File is required'},
                'files': []
            }
        
        if not key:
            return {
                'text': 'Error: Key is required',
                'json': {'success': False, 'error': 'Key is required'},
                'files': []
            }
        
        if not hasattr(file_obj, 'save_as'):
            return {
                'text': 'Error: Invalid file object',
                'json': {'success': False, 'error': 'Invalid file object'},
                'files': []
            }
        
        try:
            import tempfile
            temp_dir = tempfile.gettempdir()
            
            input_path = os.path.join(temp_dir, file_obj.filename)
            file_obj.save_as(input_path)
            
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
                return {
                    'text': f'Error: Unsupported file type. Simple decryption only supports PDF, ZIP, and 7Z files.',
                    'json': {'success': False, 'error': 'Unsupported file type'},
                    'files': []
                }
            
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
                    
                    return {
                        'text': f"File decrypted successfully with simple method.\n\nFile: {file_obj.filename}\nFile type: {file_ext.upper()}\nOutput directory: {output_filename}\nExtracted files: {len(files)}",
                        'json': {
                            'success': True,
                            'filename': file_obj.filename,
                            'file_type': file_ext.upper(),
                            'output_directory': output_filename,
                            'extracted_files_count': len(files),
                            'key': key
                        },
                        'files': []
                    }
                else:
                    output_file = {
                        'type': 'file',
                        'filename': output_filename,
                        'path': output_path
                    }
                    
                    file_size = os.path.getsize(output_path)
                    file_size_mb = file_size / (1024 * 1024)
                    
                    return {
                        'text': f"File decrypted successfully with simple method.\n\nFile: {file_obj.filename}\nDecrypted file: {output_filename}\nFile size: {file_size_mb:.2f} MB\nFile type: {file_ext.upper()}",
                        'json': {
                            'success': True,
                            'filename': file_obj.filename,
                            'decrypted_filename': output_filename,
                            'file_size_bytes': file_size,
                            'file_size_mb': round(file_size_mb, 2),
                            'file_type': file_ext.upper(),
                            'key': key
                        },
                        'files': [output_file]
                    }
            else:
                return {
                    'text': message,
                    'json': {'success': False, 'error': message},
                    'files': []
                }
        except Exception as e:
            return {
                'text': f'Error during decryption: {str(e)}',
                'json': {'success': False, 'error': str(e)},
                'files': []
            }
