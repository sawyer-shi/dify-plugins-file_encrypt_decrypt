import os
from typing import Any
from collections.abc import Generator
from dify_plugin import Tool
from dify_plugin.entities.tool import ToolInvokeMessage
from tools.crypto_utils import SecurityUtils


class DecryptFilePro(Tool):
    
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
        
        if not hasattr(file_obj, 'save_as'):
            yield self.create_text_message("Error: Invalid file object")
            yield self.create_json_message({'success': False, 'error': 'Invalid file object'})
            return
        
        try:
            import tempfile
            temp_dir = tempfile.gettempdir()
            
            input_path = os.path.join(temp_dir, file_obj.filename)
            file_obj.save_as(input_path)
            
            success, message, original_filename = SecurityUtils.decrypt_file_with_header(input_path, key, temp_dir)
            
            if success and original_filename:
                output_path = os.path.join(temp_dir, original_filename)
                file_size = os.path.getsize(output_path)
                file_size_mb = file_size / (1024 * 1024)
                
                yield self.create_text_message(f"File decrypted successfully with advanced method.\n\nEncrypted file: {file_obj.filename}\nDecrypted file: {original_filename}\nFile size: {file_size_mb:.2f} MB")
                
                yield self.create_json_message({
                    'success': True,
                    'encrypted_filename': file_obj.filename,
                    'decrypted_filename': original_filename,
                    'file_size_bytes': file_size,
                    'file_size_mb': round(file_size_mb, 2),
                    'key': key
                })
                
                yield self.create_blob_message(
                    blob=open(output_path, 'rb').read(),
                    meta={
                        'filename': original_filename,
                        'mime_type': 'application/octet-stream'
                    }
                )
            else:
                yield self.create_text_message(message)
                yield self.create_json_message({'success': False, 'error': message})
        except Exception as e:
            yield self.create_text_message(f'Error during decryption: {str(e)}')
            yield self.create_json_message({'success': False, 'error': str(e)})
