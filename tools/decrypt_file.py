import os
from typing import Any
from collections.abc import Generator
from dify_plugin import Tool
from dify_plugin.entities.tool import ToolInvokeMessage
from tools.crypto_utils import SecurityUtils


def get_mime_type(filename: str) -> str:
    ext = os.path.splitext(filename)[1].lower()
    mime_types = {
        '.pdf': 'application/pdf',
        '.zip': 'application/zip',
        '.7z': 'application/x-7z-compressed',
        '.txt': 'text/plain',
        '.doc': 'application/msword',
        '.docx': 'application/vnd.openxmlformats-officedocument.wordprocessingml.document',
        '.xls': 'application/vnd.ms-excel',
        '.xlsx': 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet',
        '.ppt': 'application/vnd.ms-powerpoint',
        '.pptx': 'application/vnd.openxmlformats-officedocument.presentationml.presentation',
        '.jpg': 'image/jpeg',
        '.jpeg': 'image/jpeg',
        '.png': 'image/png',
        '.gif': 'image/gif',
        '.bmp': 'image/bmp',
        '.mp3': 'audio/mpeg',
        '.mp4': 'video/mp4',
        '.avi': 'video/x-msvideo',
        '.mov': 'video/quicktime',
        '.wmv': 'video/x-ms-wmv',
        '.flv': 'video/x-flv',
        '.mkv': 'video/x-matroska',
        '.wav': 'audio/wav',
        '.ogg': 'audio/ogg',
        '.webm': 'video/webm',
        '.svg': 'image/svg+xml',
        '.tiff': 'image/tiff',
        '.ico': 'image/x-icon',
        '.webp': 'image/webp',
        '.json': 'application/json',
        '.xml': 'application/xml',
        '.html': 'text/html',
        '.htm': 'text/html',
        '.css': 'text/css',
        '.js': 'application/javascript',
        '.py': 'text/x-python',
        '.java': 'text/x-java-source',
        '.c': 'text/x-c',
        '.cpp': 'text/x-c++',
        '.h': 'text/x-c',
        '.hpp': 'text/x-c++',
        '.cs': 'text/x-csharp',
        '.php': 'application/x-httpd-php',
        '.rb': 'text/x-ruby',
        '.go': 'text/x-go',
        '.rs': 'text/x-rust',
        '.swift': 'text/x-swift',
        '.kt': 'text/x-kotlin',
        '.ts': 'application/typescript',
        '.tsx': 'application/typescript',
        '.jsx': 'text/jsx',
        '.vue': 'text/x-vue',
        '.sql': 'application/sql',
        '.csv': 'text/csv',
        '.md': 'text/markdown',
        '.rtf': 'application/rtf',
        '.odt': 'application/vnd.oasis.opendocument.text',
        '.ods': 'application/vnd.oasis.opendocument.spreadsheet',
        '.odp': 'application/vnd.oasis.opendocument.presentation',
        '.tar': 'application/x-tar',
        '.gz': 'application/gzip',
        '.bz2': 'application/x-bzip2',
        '.xz': 'application/x-xz',
        '.rar': 'application/vnd.rar',
        '.iso': 'application/x-iso9660-image',
        '.dmg': 'application/x-apple-diskimage',
        '.exe': 'application/x-msdownload',
        '.msi': 'application/x-msi',
        '.apk': 'application/vnd.android.package-archive',
        '.ipa': 'application/octet-stream',
        '.deb': 'application/vnd.debian.binary-package',
        '.rpm': 'application/x-rpm',
        '.sh': 'application/x-sh',
        '.bat': 'application/x-bat',
        '.ps1': 'application/x-powershell',
        '.dll': 'application/x-msdownload',
        '.so': 'application/x-sharedlib',
        '.dylib': 'application/x-mac-dylib',
        '.lib': 'application/x-library',
        '.a': 'application/x-archive',
        '.o': 'application/x-object',
        '.class': 'application/java-vm',
        '.jar': 'application/java-archive',
        '.war': 'application/java-archive',
        '.ear': 'application/java-archive',
        '.swf': 'application/x-shockwave-flash',
        '.fla': 'application/x-fla',
        '.as': 'application/x-actionscript',
        '.mxp': 'application/x-mxp',
        '.air': 'application/vnd.adobe.air-application-installer-package+zip',
        '.zxp': 'application/x-zxp',
        '.pem': 'application/x-pem-file',
        '.crt': 'application/x-x509-ca-cert',
        '.cer': 'application/x-x509-ca-cert',
        '.der': 'application/x-x509-ca-cert',
        '.p12': 'application/x-pkcs12',
        '.pfx': 'application/x-pkcs12',
        '.key': 'application/x-pem-key',
        '.pub': 'application/x-pem-key',
        '.asc': 'application/pgp-signature',
        '.sig': 'application/pgp-signature',
        '.gpg': 'application/pgp-encrypted',
        '.asc': 'application/pgp-signature',
        '.sig': 'application/pgp-signature',
        '.p7s': 'application/pkcs7-signature',
        '.p7b': 'application/x-pkcs7-certificates',
        '.p7r': 'application/x-pkcs7-certreqresp',
        '.p7c': 'application/pkcs7-mime',
        '.spc': 'application/x-pkcs7-certificates',
        '.sst': 'application/vnd.ms-pki.stl',
        '.stl': 'application/vnd.ms-pki.stl',
        '.pko': 'application/vnd.ms-pki.pko',
        '.cat': 'application/vnd.ms-pki.seccat',
        '.crl': 'application/pkix-crl',
        '.rl': 'application/resource-lists+xml',
        '.wrl': 'model/vrml',
        '.vrm': 'model/vrml',
        '.vrml': 'model/vrml',
        '.igs': 'model/iges',
        '.iges': 'model/iges',
        '.msh': 'model/mesh',
        '.mesh': 'model/mesh',
        '.silo': 'model/mesh',
        '.obj': 'application/x-tgif',
        '.mtl': 'application/x-mtl',
        '.stl': 'application/sla',
        '.dxf': 'application/dxf',
        '.dwg': 'application/acad',
        '.dwf': 'model/vnd.dwf',
        '.gbr': 'application/x-gerber',
        '.gtl': 'application/x-gerber',
        '.gbl': 'application/x-gerber',
        '.gbo': 'application/x-gerber',
        '.gbs': 'application/x-gerber',
        '.gml': 'application/x-gerber',
        '.gko': 'application/x-gerber',
        '.gm1': 'application/x-gerber',
        '.gm2': 'application/x-gerber',
        '.gm3': 'application/x-gerber',
        '.cmp': 'application/x-gerber',
        '.sol': 'application/x-gerber',
        '.stc': 'application/x-gerber',
        '.sts': 'application/x-gerber',
        '.plc': 'application/x-gerber',
        '.top': 'application/x-gerber',
        '.drd': 'application/x-gerber',
        '.art': 'application/x-gerber',
        '.rep': 'application/x-gerber',
        '': 'application/octet-stream'
    }
    return mime_types.get(ext, 'application/octet-stream')


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
                mime_type = get_mime_type(output_filename)
                
                yield self.create_text_message(f"File decrypted successfully.\n\nEncrypted file: {filename}\nDecrypted file: {output_filename}\nFile size: {file_size_mb:.2f} MB\nFile type: {mime_type}")
                
                yield self.create_json_message({
                    'success': True,
                    'encrypted_filename': filename,
                    'decrypted_filename': output_filename,
                    'file_size_bytes': file_size,
                    'file_size_mb': round(file_size_mb, 2),
                    'file_type': mime_type,
                    'key': key
                })
                
                yield self.create_blob_message(
                    blob=open(output_path, 'rb').read(),
                    meta={
                        'filename': output_filename,
                        'mime_type': mime_type
                    }
                )
            else:
                yield self.create_text_message(message)
                yield self.create_json_message({'success': False, 'error': message})
        except Exception as e:
            yield self.create_text_message(f'Error during decryption: {str(e)}')
            yield self.create_json_message({'success': False, 'error': str(e)})
