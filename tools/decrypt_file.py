import os
from typing import Any
from collections.abc import Generator
from dify_plugin import Tool
from dify_plugin.entities.tool import ToolInvokeMessage
from tools.crypto_utils import SecurityUtils


class DecryptFile(Tool):
    
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
            
            filename = file_obj.filename
            
            supported_suffixes = ['.locked', '.enc', '.secret']
            output_filename = None
            
            for suffix in supported_suffixes:
                if filename.endswith(suffix):
                    output_filename = filename[:-len(suffix)]
                    break
            
            if not output_filename:
                yield self.create_text_message(f'Error: File does not have a supported encryption suffix. Supported suffixes: {", ".join(supported_suffixes)}')
                yield self.create_json_message({'success': False, 'error': 'Invalid file format'})
                return
            
            output_path = os.path.join(temp_dir, output_filename)
            
            success, message = SecurityUtils.decrypt_file(input_path, key, output_path)
            
            if success:
                file_size = os.path.getsize(output_path)
                file_size_mb = file_size / (1024 * 1024)
                
                yield self.create_text_message(f"File decrypted successfully.\n\nEncrypted file: {filename}\nDecrypted file: {output_filename}\nFile size: {file_size_mb:.2f} MB")
                
                yield self.create_json_message({
                    'success': True,
                    'encrypted_filename': filename,
                    'decrypted_filename': output_filename,
                    'file_size_bytes': file_size,
                    'file_size_mb': round(file_size_mb, 2),
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
