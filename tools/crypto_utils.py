import base64
import hashlib
import struct
import io
from typing import Optional, Tuple
from cryptography.fernet import Fernet
import pyzipper
import pikepdf
import py7zr


class SecurityUtils:
    
    @staticmethod
    def get_fernet(key: str) -> Fernet:
        key_bytes = key.encode('utf-8')
        key_hash = hashlib.sha256(key_bytes).digest()
        key_base64 = base64.urlsafe_b64encode(key_hash)
        return Fernet(key_base64)
    
    @staticmethod
    def generate_key() -> str:
        return Fernet.generate_key().decode('utf-8')
    
    @staticmethod
    def encrypt_file(file_path: str, key: str, output_path: str) -> Tuple[bool, str]:
        try:
            fernet = SecurityUtils.get_fernet(key)
            
            with open(file_path, 'rb') as f:
                file_data = f.read()
            
            encrypted_data = fernet.encrypt(file_data)
            
            with open(output_path, 'wb') as f:
                f.write(encrypted_data)
            
            return True, f"File encrypted successfully: {output_path}"
        except Exception as e:
            return False, f"Encryption failed: {str(e)}"
    
    @staticmethod
    def decrypt_file(file_path: str, key: str, output_path: str) -> Tuple[bool, str]:
        try:
            fernet = SecurityUtils.get_fernet(key)
            
            with open(file_path, 'rb') as f:
                encrypted_data = f.read()
            
            decrypted_data = fernet.decrypt(encrypted_data)
            
            with open(output_path, 'wb') as f:
                f.write(decrypted_data)
            
            return True, f"File decrypted successfully: {output_path}"
        except Exception as e:
            return False, f"Decryption failed: {str(e)}"
    
    @staticmethod
    def encrypt_file_with_header(file_path: str, key: str, output_path: str) -> Tuple[bool, str]:
        try:
            fernet = SecurityUtils.get_fernet(key)
            
            import os
            filename = os.path.basename(file_path)
            filename_bytes = filename.encode('utf-8')
            filename_len = len(filename_bytes)
            
            with open(file_path, 'rb') as f:
                file_content = f.read()
            
            packet = struct.pack('I', filename_len) + filename_bytes + file_content
            encrypted_data = fernet.encrypt(packet)
            
            with open(output_path, 'wb') as f:
                f.write(encrypted_data)
            
            return True, f"File encrypted successfully: {output_path}"
        except Exception as e:
            return False, f"Encryption failed: {str(e)}"
    
    @staticmethod
    def decrypt_file_with_header(file_path: str, key: str, output_dir: str) -> Tuple[bool, str, Optional[str]]:
        try:
            fernet = SecurityUtils.get_fernet(key)
            
            with open(file_path, 'rb') as f:
                encrypted_data = f.read()
            
            decrypted_packet = fernet.decrypt(encrypted_data)
            
            stream = io.BytesIO(decrypted_packet)
            
            filename_len_bytes = stream.read(4)
            if not filename_len_bytes:
                return False, "Corrupted data packet", None
            
            filename_len = struct.unpack('I', filename_len_bytes)[0]
            original_filename = stream.read(filename_len).decode('utf-8')
            original_content = stream.read()
            
            import os
            output_path = os.path.join(output_dir, original_filename)
            
            with open(output_path, 'wb') as f:
                f.write(original_content)
            
            return True, f"File decrypted successfully: {output_path}", original_filename
        except Exception as e:
            return False, f"Decryption failed: {str(e)}", None
    
    @staticmethod
    def encrypt_pdf(file_path: str, key: str, output_path: str) -> Tuple[bool, str]:
        try:
            with pikepdf.open(file_path) as pdf:
                pdf.save(output_path, encryption=pikepdf.Encryption(owner=key, user=key))
            return True, f"PDF encrypted successfully: {output_path}"
        except Exception as e:
            return False, f"PDF encryption failed: {str(e)}"
    
    @staticmethod
    def decrypt_pdf(file_path: str, key: str, output_path: str) -> Tuple[bool, str]:
        try:
            with pikepdf.open(file_path, password=key) as pdf:
                pdf.save(output_path)
            return True, f"PDF decrypted successfully: {output_path}"
        except Exception as e:
            return False, f"PDF decryption failed: {str(e)}"
    
    @staticmethod
    def encrypt_zip(file_path: str, key: str, output_path: str) -> Tuple[bool, str]:
        try:
            import zipfile
            import tempfile
            import os
            
            with tempfile.TemporaryDirectory() as temp_dir:
                temp_extract_dir = os.path.join(temp_dir, 'extract')
                os.makedirs(temp_extract_dir)
                
                with zipfile.ZipFile(file_path, 'r') as zip_ref:
                    zip_ref.extractall(temp_extract_dir)
                
                with pyzipper.AESZipFile(output_path, 'w', compression=pyzipper.ZIP_DEFLATED, encryption=pyzipper.WZ_AES) as zf:
                    zf.setpassword(key.encode('utf-8'))
                    
                    for root, dirs, files in os.walk(temp_extract_dir):
                        for file in files:
                            file_path_abs = os.path.join(root, file)
                            arcname = os.path.relpath(file_path_abs, temp_extract_dir)
                            zf.write(file_path_abs, arcname)
            
            return True, f"ZIP encrypted successfully: {output_path}"
        except Exception as e:
            return False, f"ZIP encryption failed: {str(e)}"
    
    @staticmethod
    def decrypt_zip(file_path: str, key: str, output_path: str) -> Tuple[bool, str]:
        try:
            with pyzipper.AESZipFile(file_path, 'r') as zf:
                zf.setpassword(key.encode('utf-8'))
                zf.extractall(output_path)
            return True, f"ZIP decrypted successfully: {output_path}"
        except Exception as e:
            return False, f"ZIP decryption failed: {str(e)}"
    
    @staticmethod
    def encrypt_7z(file_path: str, key: str, output_path: str) -> Tuple[bool, str]:
        try:
            import os
            import tempfile
            
            with tempfile.TemporaryDirectory() as temp_dir:
                temp_extract_dir = os.path.join(temp_dir, 'extract')
                os.makedirs(temp_extract_dir)
                
                with py7zr.SevenZipFile(file_path, mode='r', password=None) as archive:
                    archive.extractall(path=temp_extract_dir)
                
                with py7zr.SevenZipFile(output_path, mode='w', password=key) as archive:
                    archive.writeall(temp_extract_dir, '')
            
            return True, f"7Z encrypted successfully: {output_path}"
        except Exception as e:
            return False, f"7Z encryption failed: {str(e)}"
    
    @staticmethod
    def decrypt_7z(file_path: str, key: str, output_path: str) -> Tuple[bool, str]:
        try:
            import os
            os.makedirs(output_path, exist_ok=True)
            
            with py7zr.SevenZipFile(file_path, mode='r', password=key) as archive:
                archive.extractall(path=output_path)
            return True, f"7Z decrypted successfully: {output_path}"
        except Exception as e:
            return False, f"7Z decryption failed: {str(e)}"
