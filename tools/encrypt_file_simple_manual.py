import os
from typing import Any
from collections.abc import Generator
from dify_plugin import Tool
from dify_plugin.entities.tool import ToolInvokeMessage
from tools.crypto_utils import SecurityUtils


class EncryptFileSimpleManual(Tool):
    
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
            output_path = os.path.join(temp_dir, f"encrypted_{file_obj.filename}")
            
            with open(input_path, 'wb') as f:
                f.write(file_obj.blob)
            
            file_ext = os.path.splitext(file_obj.filename)[1].lower()
            
            if file_ext == '.pdf':
                success, message = SecurityUtils.encrypt_pdf(input_path, key, output_path)
            elif file_ext == '.zip':
                success, message = SecurityUtils.encrypt_zip(input_path, key, output_path)
            elif file_ext == '.7z':
                success, message = SecurityUtils.encrypt_7z(input_path, key, output_path)
            else:
                yield self.create_text_message(f'Error: Unsupported file type. Simple encryption only supports PDF, ZIP, and 7Z files.')
                yield self.create_json_message({'success': False, 'error': 'Unsupported file type'})
                return
            
            if success:
                file_size = os.path.getsize(output_path)
                file_size_mb = file_size / (1024 * 1024)
                
                yield self.create_text_message(f"File encrypted successfully with simple method.\n\nFile: {file_obj.filename}\nFile size: {file_size_mb:.2f} MB\nFile type: {file_ext.upper()}\n\nNote: The file is encrypted with password protection. You will need the key to open it.")
                
                yield self.create_json_message({
                    'success': True,
                    'filename': file_obj.filename,
                    'file_size_bytes': file_size,
                    'file_size_mb': round(file_size_mb, 2),
                    'file_type': file_ext.upper()
                })
                
                yield self.create_blob_message(
                    blob=open(output_path, 'rb').read(),
                    meta={
                        'filename': file_obj.filename,
                        'mime_type': 'application/octet-stream'
                    }
                )
            else:
                yield self.create_text_message(message)
                yield self.create_json_message({'success': False, 'error': message})
        except Exception as e:
            yield self.create_text_message(f'Error during encryption: {str(e)}')
            yield self.create_json_message({'success': False, 'error': str(e)})
