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
    def _contains_cjk(text: str) -> bool:
        import re
        return bool(re.search(r'[\u4e00-\u9fff]', text))

    @staticmethod
    def _normalize_zip_filename(filename: str, flag_bits: int) -> str:
        # If UTF-8 flag is set or filename already contains CJK, keep as-is.
        if flag_bits & 0x800:
            return filename
        if SecurityUtils._contains_cjk(filename):
            return filename

        # Try to recover mojibake from CP437 to GBK/UTF-8.
        for encoding in ("gbk", "utf-8"):
            try:
                decoded = filename.encode("cp437").decode(encoding)
                if SecurityUtils._contains_cjk(decoded):
                    return decoded
            except Exception:
                continue

        return filename
    
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
        """
        加密ZIP文件，支持中文文件名
        通过临时目录解压原始文件，然后使用AES加密重新打包
        """
        try:
            import zipfile
            import tempfile
            import os
            
            with tempfile.TemporaryDirectory() as temp_dir:
                temp_extract_dir = os.path.join(temp_dir, 'extract')
                os.makedirs(temp_extract_dir)
                
                # 第一步：解压原始ZIP文件，处理可能的编码问题
                with zipfile.ZipFile(file_path, 'r') as zip_ref:
                    for info in zip_ref.infolist():
                        if not info.is_dir():
                            # 尝试修复文件名编码问题
                            fixed_filename = SecurityUtils._normalize_zip_filename(
                                info.filename,
                                getattr(info, "flag_bits", 0),
                            )
                            
                            # 提取文件到临时目录
                            extract_path = os.path.join(temp_extract_dir, fixed_filename)
                            os.makedirs(os.path.dirname(extract_path), exist_ok=True)
                            with open(extract_path, 'wb') as f:
                                f.write(zip_ref.read(info))
                
                # 第二步：使用AES加密打包文件，明确使用UTF-8编码
                with pyzipper.AESZipFile(
                    output_path, 
                    'w', 
                    compression=pyzipper.ZIP_DEFLATED, 
                    encryption=pyzipper.WZ_AES
                ) as zf:
                    zf.setpassword(key.encode('utf-8'))
                    
                    # 遍历临时目录，将所有文件加入加密ZIP
                    for root, dirs, files in os.walk(temp_extract_dir):
                        for file in files:
                            file_path_abs = os.path.join(root, file)
                            # 计算相对路径，保持目录结构
                            arcname = os.path.relpath(file_path_abs, temp_extract_dir)
                            
                            # 确保arcname使用正斜杠（ZIP标准）
                            arcname = arcname.replace(os.sep, '/')

                            # 使用当前 AESZipFile 的 ZipInfo 类型，避免类型不匹配
                            # 由 pyzipper 自动处理 UTF-8 文件名标志位
                            zinfo = zf.zipinfo_cls(arcname)
                            zinfo.compress_type = pyzipper.ZIP_DEFLATED

                            with open(file_path_abs, 'rb') as f:
                                zf.writestr(zinfo, f.read())
            
            return True, f"ZIP encrypted successfully: {output_path}"
        except Exception as e:
            return False, f"ZIP encryption failed: {str(e)}"
    
    @staticmethod
    def decrypt_zip(file_path: str, key: str, output_path: str) -> Tuple[bool, str]:
        """
        解密ZIP文件，支持中文文件名
        自动处理文件名编码问题，确保中文文件名正确解压
        """
        try:
            import os
            os.makedirs(output_path, exist_ok=True)
            
            with pyzipper.AESZipFile(file_path, 'r') as zf:
                zf.setpassword(key.encode('utf-8'))
                
                # 遍历压缩包中的所有文件
                for info in zf.infolist():
                    if not info.is_dir():
                        # 处理文件名编码问题
                        fixed_filename = SecurityUtils._normalize_zip_filename(
                            info.filename,
                            getattr(info, "flag_bits", 0),
                        )
                        
                        # 构造完整的输出路径
                        extract_path = os.path.join(output_path, fixed_filename)
                        # 确保目录存在
                        os.makedirs(os.path.dirname(extract_path), exist_ok=True)
                        
                        # 解密并写入文件
                        with open(extract_path, 'wb') as f:
                            f.write(zf.read(info))
            
            return True, f"ZIP decrypted successfully: {output_path}"
        except Exception as e:
            return False, f"ZIP decryption failed: {str(e)}"
    
    @staticmethod
    def encrypt_7z(file_path: str, key: str, output_path: str) -> Tuple[bool, str]:
        """
        加密7Z文件，支持中文文件名
        通过临时目录解压原始文件，然后使用密码重新打包
        """
        try:
            import os
            import tempfile
            
            with tempfile.TemporaryDirectory() as temp_dir:
                temp_extract_dir = os.path.join(temp_dir, 'extract')
                os.makedirs(temp_extract_dir)
                
                # 第一步：解压原始7Z文件
                with py7zr.SevenZipFile(file_path, mode='r') as archive:
                    archive.extractall(path=temp_extract_dir)
                
                # 第二步：使用密码重新打包
                with py7zr.SevenZipFile(output_path, mode='w', password=key) as archive:
                    # 遍历临时目录，逐个添加文件
                    for root, dirs, files in os.walk(temp_extract_dir):
                        for file in files:
                            file_path_abs = os.path.join(root, file)
                            arcname = os.path.relpath(file_path_abs, temp_extract_dir)
                            # 使用正确的路径分隔符（7z使用/）
                            arcname = arcname.replace(os.sep, '/')
                            archive.write(file_path_abs, arcname)
            
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
