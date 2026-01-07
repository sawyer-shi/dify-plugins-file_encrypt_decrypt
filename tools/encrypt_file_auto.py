import os
from typing import Any
from collections.abc import Generator
from dify_plugin import Tool
from dify_plugin.entities.tool import ToolInvokeMessage
from tools.crypto_utils import SecurityUtils


class EncryptFileAuto(Tool):
    
    def _invoke(self, parameters: dict[str, Any]) -> Generator[ToolInvokeMessage]:
        file_obj = parameters.get('file')
        suffix = parameters.get('suffix', 'locked')
        
        if not file_obj:
            yield self.create_text_message("Error: File is required")
            yield self.create_json_message({'success': False, 'error': 'File is required'})
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
            
            key = SecurityUtils.generate_key()
            
            base_name, ext = os.path.splitext(file_obj.filename)
            output_filename = f"{base_name}{ext}.{suffix}"
            output_path = os.path.join(temp_dir, output_filename)
            
            success, message = SecurityUtils.encrypt_file(input_path, key, output_path)
            
            if success:
                file_size = os.path.getsize(output_path)
                file_size_mb = file_size / (1024 * 1024)
                
                yield self.create_text_message(f"File encrypted successfully.\n\nOriginal file: {file_obj.filename}\nEncrypted file: {output_filename}\nFile size: {file_size_mb:.2f} MB\nEncryption suffix: {suffix}\n\nIMPORTANT: Save this key for decryption:\n{key}")
                
                yield self.create_json_message({
                    'success': True,
                    'original_filename': file_obj.filename,
                    'encrypted_filename': output_filename,
                    'file_size_bytes': file_size,
                    'file_size_mb': round(file_size_mb, 2),
                    'encryption_suffix': suffix,
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
            yield self.create_text_message(f'Error during encryption: {str(e)}')
            yield self.create_json_message({'success': False, 'error': str(e)})
