import os
from typing import Any
from collections.abc import Generator
from dify_plugin import Tool
from dify_plugin.entities.tool import ToolInvokeMessage
from tools.crypto_utils import SecurityUtils


def get_mime_type(filename: str) -> str:
    """
    根据文件扩展名获取MIME类型
    支持常见的文件类型
    """
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
        '.json': 'application/json',
        '.xml': 'application/xml',
        '.html': 'text/html',
        '.css': 'text/css',
        '.js': 'application/javascript'
    }
    return mime_types.get(ext, 'application/octet-stream')


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
                    # 解密成功后，遍历输出目录获取所有解密的文件
                    # SecurityUtils.decrypt_zip 或 decrypt_7z 已经完成解密
                    extracted_files = []
                    
                    # 遍历整个输出目录树，收集所有文件
                    for root, dirs, file_list in os.walk(output_path):
                        for file in file_list:
                            file_path_abs = os.path.join(root, file)
                            rel_path = os.path.relpath(file_path_abs, output_path)
                            extracted_files.append((rel_path, file_path_abs))
                    
                    # 生成文件列表用于显示
                    files = [f[0] for f in extracted_files]
                    files_list = '\n  - '.join(files[:20])
                    if len(files) > 20:
                        files_list += f'\n  ... and {len(files) - 20} more files'
                    
                    if len(extracted_files) == 1:
                        # 只有一个文件，直接返回该文件
                        rel_path, file_path_abs = extracted_files[0]
                        file_size = os.path.getsize(file_path_abs)
                        file_size_mb = file_size / (1024 * 1024)
                        mime_type = get_mime_type(rel_path)
                        
                        yield self.create_text_message(
                            f"File decrypted successfully with simple method.\n\n"
                            f"File: {file_obj.filename}\n"
                            f"File type: {file_ext.upper()}\n"
                            f"Output directory: {output_path}\n"
                            f"Extracted file: {rel_path}\n"
                            f"File size: {file_size_mb:.2f} MB\n"
                            f"MIME type: {mime_type}"
                        )
                        
                        yield self.create_json_message({
                            'success': True,
                            'filename': file_obj.filename,
                            'file_type': file_ext.upper(),
                            'output_directory': output_path,
                            'extracted_files_count': 1,
                            'extracted_file': rel_path,
                            'file_size_bytes': file_size,
                            'file_size_mb': round(file_size_mb, 2),
                            'mime_type': mime_type,
                            'key': key
                        })
                        
                        yield self.create_blob_message(
                            blob=open(file_path_abs, 'rb').read(),
                            meta={
                                'filename': rel_path,
                                'mime_type': mime_type
                            }
                        )
                    else:
                        # 多个文件，返回每个文件作为独立blob
                        # 计算总大小
                        total_size = sum(os.path.getsize(f[1]) for f in extracted_files)
                        total_size_mb = total_size / (1024 * 1024)
                        
                        # 生成文件列表，确保正确显示中文文件名
                        files_info = []
                        for rel_path, file_path_abs in extracted_files:
                            file_size = os.path.getsize(file_path_abs)
                            file_size_kb = file_size / 1024
                            # 确保文件名正确编码为UTF-8
                            display_name = rel_path
                            files_info.append(f"{display_name} ({file_size_kb:.2f} KB)")
                        
                        files_list_text = '\n  - '.join(files_info[:20])
                        if len(files_info) > 20:
                            files_list_text += f'\n  ... and {len(files_info) - 20} more files'
                        
                        yield self.create_text_message(
                            f"File decrypted successfully with simple method.\n\n"
                            f"File: {file_obj.filename}\n"
                            f"File type: {file_ext.upper()}\n"
                            f"Output directory: {output_path}\n"
                            f"Extracted files: {len(extracted_files)}\n"
                            f"Total size: {total_size_mb:.2f} MB\n\n"
                            f"File list:\n  - {files_list_text}\n\n"
                            f"Note: All files are available below."
                        )
                        
                        yield self.create_json_message({
                            'success': True,
                            'filename': file_obj.filename,
                            'file_type': file_ext.upper(),
                            'output_directory': output_path,
                            'extracted_files_count': len(extracted_files),
                            'extracted_files': [f[0] for f in extracted_files],
                            'total_size_bytes': total_size,
                            'total_size_mb': round(total_size_mb, 2),
                            'key': key
                        })
                        
                        # 返回每个文件作为独立blob
                        for rel_path, file_path_abs in extracted_files:
                            mime_type = get_mime_type(rel_path)
                            # 使用文件的basename作为输出文件名
                            output_filename = os.path.basename(rel_path)
                            
                            yield self.create_blob_message(
                                blob=open(file_path_abs, 'rb').read(),
                                meta={
                                    'filename': output_filename,
                                    'mime_type': mime_type
                                }
                            )
                else:
                    file_size = os.path.getsize(output_path)
                    file_size_mb = file_size / (1024 * 1024)
                    
                    mime_type_map = {
                        '.pdf': 'application/pdf',
                        '.zip': 'application/zip',
                        '.7z': 'application/x-7z-compressed'
                    }
                    mime_type = mime_type_map.get(file_ext, 'application/octet-stream')
                    
                    yield self.create_text_message(f"File decrypted successfully with simple method.\n\nFile: {file_obj.filename}\nDecrypted file: {output_filename}\nFile size: {file_size_mb:.2f} MB\nFile type: {file_ext.upper()}")
                    
                    yield self.create_json_message({
                        'success': True,
                        'filename': file_obj.filename,
                        'decrypted_filename': output_filename,
                        'file_size_bytes': file_size,
                        'file_size_mb': round(file_size_mb, 2),
                        'file_type': file_ext.upper(),
                        'mime_type': mime_type,
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
