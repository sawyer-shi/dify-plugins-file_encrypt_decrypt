# Privacy Policy / 隐私政策

**Effective Date / 生效日期**: January 14, 2026 / 2026年1月14日
**Version / 版本**: v0.0.1
**Plugin Name / 插件名称**: File Encrypt & Decrypt / 文件加密与解密工具
**License / 许可证**: Apache License 2.0

---

## English Version

### Overview

The File Encrypt & Decrypt Plugin ("Plugin") is designed to facilitate local file encryption and decryption operations while prioritizing user privacy and data security. This privacy policy explains how we handle your data when you use our plugin within the Dify platform.

### License Information

This plugin is licensed under the Apache License 2.0, which is a permissive open-source license that allows for the use, modification, and distribution of the software. The full license text is available in the LICENSE file included with this plugin.

### Data Collection

**What we DO NOT collect:**
- Personal identification information
- User account details
- Usage analytics or tracking data
- Device information
- Location data
- Cookies or similar tracking technologies

**What we process:**
- Files you choose to encrypt or decrypt
- File metadata (e.g., filename, size, format) required for encryption/decryption operations
- Encryption/decryption keys (passwords) provided by you
- Temporary processing data required for encryption/decryption operations

### Data Processing

**Local Processing:**
- All file encryption and decryption operations are performed locally on your system without external data transmission
- No files are uploaded to external servers during any encryption or decryption operation
- Temporary files are created and deleted securely during processing
- No API keys or external services are required for any operations

### Data Storage

**No Data Retention:**
- We do not store or retain copies of your files after encryption or decryption
- We do not access or view the contents of your files beyond what is necessary for the requested operations
- Temporary files are automatically deleted after the processing completes
- No data is transmitted to any third-party services

### Security Measures

**Data Protection:**
- All file encryption and decryption is performed in a secure local environment
- No network connections are made for file operations
- Temporary files are handled with appropriate security measures
- No external API calls or service dependencies
- Encryption keys are processed locally and never transmitted

### Supported Operations

The plugin supports the following file encryption and decryption operations, all performed locally:

1. **Simple Encryption (Manual Key)**: Encrypt PDF, ZIP, or 7Z files with a manually provided key
2. **Simple Encryption (Auto-generated Key)**: Encrypt PDF, ZIP, or 7Z files with an automatically generated key
3. **Pro Encryption (Manual Key)**: Encrypt any file type with a manually provided key and custom suffix (locked, enc, secret)
4. **Pro Encryption (Auto-generated Key)**: Encrypt any file type with an automatically generated key and custom suffix (locked, enc, secret)
5. **Normal Encryption (Manual Key)**: Encrypt any file type with a manually provided key and custom suffix (locked, enc, secret)
6. **Normal Encryption (Auto-generated Key)**: Encrypt any file type with an automatically generated key and custom suffix (locked, enc, secret)
7. **Simple Decryption**: Decrypt PDF, ZIP, or 7Z files that were encrypted with the simple encryption method
8. **Pro Decryption**: Decrypt files with suffixes locked, enc, or secret into their original formats
9. **Normal Decryption**: Decrypt files with suffixes like .pdf.locked, .mp4.enc, .xlsx.secret into their original formats

All operations are executed entirely on your local machine without any external dependencies.

### Contact Information

**Developer:** `https://github.com/sawyer-shi`
**Email:** sawyer36@foxmail.com
**Source Code:** `https://github.com/sawyer-shi/dify-plugins-file_encrypt_decrypt`
**Support:** Available through Dify platform and GitHub Issues

---

## 中文版本

### 概述

文件加密与解密工具插件（"插件"）旨在促进本地文件加密和解密操作，同时优先保护用户隐私和数据安全。本隐私政策说明了您在Dify平台内使用我们的插件时，我们如何处理您的数据。

### 许可证信息

本插件采用Apache License 2.0许可证，这是一个宽松的开源许可证，允许使用、修改和分发软件。完整的许可证文本可在本插件附带的LICENSE文件中找到。

### 数据收集

**我们不收集的内容：**
- 个人身份信息
- 用户账户详细信息
- 使用分析或跟踪数据
- 设备信息
- 位置数据
- Cookie或类似跟踪技术

**我们处理的内容：**
- 您选择加密或解密的文件
- 加密/解密操作所需的文件元数据（如文件名、大小、格式）
- 您提供的加密/解密密钥（密码）
- 加密/解密操作所需的临时处理数据

### 数据处理

**本地处理：**
- 所有文件加密和解密操作都在您的系统上本地执行，无需外部数据传输
- 任何加密或解密过程中都不会将文件上传到外部服务器
- 处理过程中会安全地创建和删除临时文件
- 任何操作都不需要API密钥或外部服务

### 数据存储

**不保留数据：**
- 加密或解密完成后，我们不存储或保留您文件的副本
- 除了请求的操作所需的内容外，我们不访问或查看您文件的内容
- 处理过程完成后，临时文件会自动删除
- 不会将任何数据传输到第三方服务

### 安全措施

**数据保护：**
- 所有文件加密和解密都在安全的本地环境中执行
- 文件操作不会建立网络连接
- 临时文件通过适当的安全措施进行处理
- 无外部API调用或服务依赖
- 加密密钥在本地处理，从不传输

### 支持的操作

插件支持以下文件加密和解密操作，全部在本地执行：

1. **简单加密（手动密钥）**：使用手动提供的密钥加密PDF、ZIP或7Z文件
2. **简单加密（自动生成密钥）**：使用自动生成的密钥加密PDF、ZIP或7Z文件
3. **高级加密（手动密钥）**：使用手动提供的密钥和自定义后缀（locked、enc、secret）加密任何类型文件
4. **高级加密（自动生成密钥）**：使用自动生成的密钥和自定义后缀（locked、enc、secret）加密任何类型文件
5. **通用加密（手动密钥）**：使用手动提供的密钥和自定义后缀（locked、enc、secret）加密任何类型文件
6. **通用加密（自动生成密钥）**：使用自动生成的密钥和自定义后缀（locked、enc、secret）加密任何类型文件
7. **简单解密**：解密使用简单加密方法加密的PDF、ZIP或7Z文件
8. **高级解密**：将带有locked、enc或secret后缀的文件解密为原始格式
9. **通用解密**：将带有.pdf.locked、.mp4.enc、.xlsx.secret等后缀的文件解密为原始格式

所有操作完全在您的本地机器上执行，无需任何外部依赖。

### 联系信息

**开发者：** `https://github.com/sawyer-shi`
**邮箱：** sawyer36@foxmail.com
**项目代码来源：** `https://github.com/sawyer-shi/dify-plugins-file_encrypt_decrypt`
**支持：** 通过Dify平台和GitHub Issues提供

---

**最后更新：** 2026年1月14日
