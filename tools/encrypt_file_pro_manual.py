import os
from typing import Any
from collections.abc import Generator
from dify_plugin import Tool
from dify_plugin.entities.tool import ToolInvokeMessage
from tools.crypto_utils import SecurityUtils


class EncryptFileProManual(Tool):
    
    def _invoke(self, parameters: dict[str, Any]) -> Generator[ToolInvokeMessage]:
        file_obj = parameters.get('file')
        key = parameters.get('key')
        suffix = parameters.get('suffix', 'locked')
        
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
            
            base_name = os.path.splitext(file_obj.filename)[0]
            output_filename = f"{base_name}.{suffix}"
            output_path = os.path.join(temp_dir, output_filename)
            
            success, message = SecurityUtils.encrypt_file_with_header(input_path, key, output_path)
            
            if success:
                file_size = os.path.getsize(output_path)
                file_size_mb = file_size / (1024 * 1024)
                
                yield self.create_text_message(f"File encrypted successfully with advanced method.\n\nOriginal file: {file_obj.filename}\nEncrypted file: {output_filename}\nFile size: {file_size_mb:.2f} MB\nEncryption suffix: {suffix}\n\nNote: Original filename is embedded in the encrypted file.")
                
                yield self.create_json_message({
                    'success': True,
                    'original_filename': file_obj.filename,
                    'encrypted_filename': output_filename,
                    'file_size_bytes': file_size,
                    'file_size_mb': round(file_size_mb, 2),
                    'encryption_suffix': suffix
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
