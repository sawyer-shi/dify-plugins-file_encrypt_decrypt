# 文件加密与解密工具

一个功能强大的 Dify 插件，提供全面的**本地**文件加密和解密功能。所有文件操作均在您的本地机器上完全执行，无需任何外部服务、API 密钥或网络连接，确保最大的数据安全和隐私。支持各种文件格式的加密和解密，并可自定义加密后缀。

支持的文件类型包括: .pdf, .txt, .doc, .docx, .xls, .xlsx, .ppt, .pptx, .rtf, .odt, .ods, .odp, .md, .csv, .html, .htm, .css, .js, .json, .xml, .py, .java, .c, .cpp, .h, .hpp, .cs, .php, .rb, .go, .rs, .swift, .kt, .ts, .tsx, .jsx, .vue, .sql, .jpg, .jpeg, .png, .gif, .bmp, .svg, .tiff, .ico, .webp, .mp3, .wav, .ogg, .mp4, .avi, .mov, .wmv, .flv, .mkv, .webm, .zip, .7z, .tar, .gz, .bz2, .xz, .rar, .iso, .dmg, .exe, .msi, .apk, .ipa, .deb, .rpm, .sh, .bat, .ps1, .dll, .so, .dylib, .lib, .a, .o, .class, .jar, .war, .ear, .swf, .fla, .as, .mxp, .air, .zxp, .pem, .crt, .cer, .der, .p12, .pfx, .key, .pub, .asc, .sig, .gpg, .p7s, .p7b, .p7r, .p7c, .spc, .sst, .stl, .pko, .cat, .crl, .rl, .wrl, .vrm, .vrml, .igs, .iges, .msh, .mesh, .silo, .obj, .mtl, .stl, .dxf, .dwg, .dwf, .gbr, .gtl, .gbl, .gbo, .gbs, .gml, .gko, .gm1, .gm2, .gm3, .cmp, .sol, .stc, .sts, .plc, .top, .drd, .art, .rep, 以及更多。

## 版本信息

- **当前版本**: v0.0.1
- **发布日期**: 2026-01-14
- **兼容性**: Dify 插件框架
- **Python 版本**: 3.12

### 版本历史
- **v0.0.1** (2026-01-14): 初始版本，支持文件加密和解密功能

## 快速开始

1. 从 Dify 应用市场下载 file_encrypt_decrypt 插件
2. 在您的 Dify 环境中安装插件
3. 立即开始加密和解密您的文件

## 核心特性

- **100% 本地处理**: 所有文件加密和解密操作均在您的本地机器上完全执行
- **无需外部服务**: 无需连接任何外部服务或第三方 API
- **无需 API 密钥**: 完全免费使用，无需任何 API 密钥配置
- **最大数据安全**: 您的文件永远不会离开本地环境，确保完全的隐私和安全
- **零网络依赖**: 无需互联网连接即可离线工作
- **自定义加密后缀**: 可从 locked、enc 或 secret 后缀中选择用于加密文件
- **灵活的密钥管理**: 支持手动输入密钥和自动生成密钥

## 技术优势

- **本地处理**: 所有文件加密和解密均在本地执行，无外部依赖
- **高安全性**: 使用强加密算法保护您的文件
- **灵活选项**: 为不同用例提供各种配置选项
- **错误处理**: 强大的错误处理和信息提示
- **安全处理**: 文件安全处理，不保留数据
- **可自定义后缀**: 选择加密后缀以组织加密文件

## 系统要求

- Python 3.12
- Dify 平台访问权限
- 所需的 Python 包（通过 requirements.txt 安装）

## 使用方法

如果您想在 Dify 中添加其他文件类型，请添加您需要的所有文件类型：
<img width="1508" height="1874" alt="file-type" src="https://github.com/user-attachments/assets/afb3b41f-b97d-4d20-8b92-3b9e47337e89" />

该插件提供以下工具：

### 1. 文件简单加密 -- 手动密钥 (encrypt_file_simple_manual)
使用手动提供的密钥加密 PDF、ZIP 或 7Z 文件。
- **参数**:
  - `file`: 要加密的文件（必需）
  - `key`: 加密密钥（必需）
- **功能**:
  - 支持 PDF、ZIP、7Z 文件
  - 手动输入密钥
  - 密码保护
  - 显示文件大小和类型
  - 输出加密文件
<img width="2156" height="1303" alt="simple-A-01" src="https://github.com/user-attachments/assets/9bf00078-7d63-4468-9894-f9c1a48ed301" />

### 2. 文件简单加密 -- 自动密钥 (encrypt_file_simple_auto)
使用自动生成的密钥加密 PDF、ZIP 或 7Z 文件。
- **参数**:
  - `file`: 要加密的文件（必需）
- **功能**:
  - 支持 PDF、ZIP、7Z 文件
  - 自动生成密钥
  - 加密后显示密钥
  - 密码保护
  - 显示文件大小和类型
  - 输出加密文件
<img width="2256" height="1273" alt="simple-B-01" src="https://github.com/user-attachments/assets/ca2352ea-c581-4dcf-a1cc-93bc61e15d74" />

### 3. 文件简单解密 (decrypt_file_simple)
解密使用简单加密方法加密的 PDF、ZIP 或 7Z 文件。
- **参数**:
  - `file`: 要解密的加密文件（必需）
  - `key`: 解密密钥（必需）
- **功能**:
  - 支持 PDF、ZIP、7Z 文件
  - 需要密钥
  - 自动文件类型检测
  - 输出正确的文件类型
  - 显示文件大小和类型
<img width="2513" height="1388" alt="simple-C-01" src="https://github.com/user-attachments/assets/67c964d8-b1c9-445c-9116-517b499a06b7" />
<img width="791" height="375" alt="simple-C-02" src="https://github.com/user-attachments/assets/ebbc8e02-7037-4fe3-b02e-d913b6a27641" />
<img width="2524" height="1309" alt="simple-C-03" src="https://github.com/user-attachments/assets/3c72fa50-dccd-4f2a-a4fb-500af434b7ba" />

### 4. 文件通用加密 -- 手动密钥 (encrypt_file_manual)
使用手动提供的密钥和自定义后缀加密任何文件类型。
- **参数**:
  - `file`: 要加密的文件（必需）
  - `key`: 加密密钥（必需）
  - `suffix`: 加密后缀（可选，默认：locked）
    - `locked`: .locked 后缀
    - `enc`: .enc 后缀
    - `secret`: .secret 后缀
- **功能**:
  - 支持任何文件类型
  - 手动输入密钥
  - 自定义后缀选择
  - 密码保护
  - 显示文件大小和类型
  - 输出带有自定义后缀的加密文件
<img width="2645" height="964" alt="normal-A-01" src="https://github.com/user-attachments/assets/f6860cb9-0cf4-4fb1-aa3a-cc0c0a9858a0" />

### 5. 文件通用加密 -- 自动密钥 (encrypt_file_auto)
使用自动生成的密钥和自定义后缀加密任何文件类型。
- **参数**:
  - `file`: 要加密的文件（必需）
  - `suffix`: 加密后缀（可选，默认：locked）
    - `locked`: .locked 后缀
    - `enc`: .enc 后缀
    - `secret`: .secret 后缀
- **功能**:
  - 支持任何文件类型
  - 自动生成密钥
  - 加密后显示密钥
  - 自定义后缀选择
  - 密码保护
  - 显示文件大小和类型
  - 输出带有自定义后缀的加密文件
<img width="2349" height="1165" alt="normal-B-01" src="https://github.com/user-attachments/assets/2382469f-b0b1-47a0-adcf-07669b38a057" />

### 6. 文件通用解密 (decrypt_file)
将带有 .pdf.locked、.mp4.enc、.xlsx.secret 等后缀的文件解密为原始格式。
- **参数**:
  - `file`: 要解密的加密文件（必需）
  - `key`: 解密密钥（必需）
- **功能**:
  - 支持任何加密文件
  - 需要密钥
  - 自动文件类型检测
  - 输出正确的文件类型
  - 显示文件大小和类型
<img width="2584" height="1606" alt="normal-C-01" src="https://github.com/user-attachments/assets/313cbf73-6f3d-4d92-bb26-bae9be5e76fc" />
<img width="2442" height="1468" alt="normal-C-02" src="https://github.com/user-attachments/assets/3d83d307-5003-46e8-9459-faa87c34981d" />

### 7. 文件高级加密 -- 手动密钥 (encrypt_file_pro_manual)
使用手动提供的密钥和自定义后缀加密任何文件类型。
- **参数**:
  - `file`: 要加密的文件（必需）
  - `key`: 加密密钥（必需）
  - `suffix`: 加密后缀（可选，默认：locked）
    - `locked`: .locked 后缀
    - `enc`: .enc 后缀
    - `secret`: .secret 后缀
- **功能**:
  - 支持任何文件类型
  - 手动输入密钥
  - 自定义后缀选择
  - 密码保护
  - 显示文件大小和类型
  - 输出带有自定义后缀的加密文件
<img width="2330" height="1061" alt="pro-A-01" src="https://github.com/user-attachments/assets/3db1441d-cc4d-428e-84af-5cf835b9b037" />

### 8. 文件高级加密 -- 自动密钥 (encrypt_file_pro_auto)
使用自动生成的密钥和自定义后缀加密任何文件类型。
- **参数**:
  - `file`: 要加密的文件（必需）
  - `suffix`: 加密后缀（可选，默认：locked）
    - `locked`: .locked 后缀
    - `enc`: .enc 后缀
    - `secret`: .secret 后缀
- **功能**:
  - 支持任何文件类型
  - 自动生成密钥
  - 加密后显示密钥
  - 自定义后缀选择
  - 密码保护
  - 显示文件大小和类型
  - 输出带有自定义后缀的加密文件
<img width="2351" height="1234" alt="pro-B-01" src="https://github.com/user-attachments/assets/327f0df5-dc8d-42d0-8d37-ed45d75aa771" />

### 9. 文件高级解密 (decrypt_file_pro)
将带有 locked、enc 或 secret 后缀的文件解密为原始格式。
- **参数**:
  - `file`: 要解密的加密文件（必需）
  - `key`: 解密密钥（必需）
- **功能**:
  - 支持任何加密文件
  - 需要密钥
  - 自动文件类型检测
  - 输出正确的文件类型
  - 显示文件大小和类型
<img width="2378" height="1095" alt="pro-C-01" src="https://github.com/user-attachments/assets/18e4c481-8cfd-4006-9a49-dec7884e17f2" />
<img width="2448" height="1642" alt="pro-C-02" src="https://github.com/user-attachments/assets/e8c70a9c-0039-40a3-8243-d36dcc26b195" />

## 注意事项

- 所有文件加密和解密均在本地执行，无需将文件上传到外部服务
- 对于自动生成的密钥，请务必保存密钥，因为解密时需要使用
- 加密和解密必须使用相同的密钥
- 简单加密仅支持 PDF、ZIP 和 7Z 文件
- 高级加密和通用加密支持任何文件类型
- 加密文件将附加所选后缀（locked、enc 或 secret）
- 大文件可能需要更长的处理时间，具体取决于其大小

## 核心功能

### 1. 简单加密

#### 简单加密 - 手动密钥
- **加密 PDF、ZIP、7Z 文件**: 使用手动提供的密钥加密 PDF、ZIP 或 7Z 文件
- **密码保护**: 文件使用密码保护进行加密
- **需要密钥**: 您必须提供密钥才能加密文件
- **支持格式**: PDF、ZIP、7Z

#### 简单加密 - 自动生成密钥
- **加密 PDF、ZIP、7Z 文件**: 使用自动生成的密钥加密 PDF、ZIP 或 7Z 文件
- **自动密钥生成**: 系统自动生成安全的密钥
- **密钥显示**: 加密后显示生成的密钥
- **保存您的密钥**: 重要：保存生成的密钥以便稍后打开文件
- **支持格式**: PDF、ZIP、7Z

### 2. 高级加密

#### 高级加密 - 手动密钥
- **加密任何文件类型**: 使用手动提供的密钥加密任何文件格式
- **自定义后缀支持**: 可从 locked、enc 或 secret 后缀中选择
- **密码保护**: 文件使用密码保护进行加密
- **需要密钥**: 您必须提供密钥才能加密文件
- **灵活的文件支持**: 适用于任何文件类型

#### 高级加密 - 自动生成密钥
- **加密任何文件类型**: 使用自动生成的密钥加密任何文件格式
- **自定义后缀支持**: 可从 locked、enc 或 secret 后缀中选择
- **自动密钥生成**: 系统自动生成安全的密钥
- **密钥显示**: 加密后显示生成的密钥
- **保存您的密钥**: 重要：保存生成的密钥以便稍后打开文件
- **灵活的文件支持**: 适用于任何文件类型

### 3. 通用加密

#### 通用加密 - 手动密钥
- **加密任何文件类型**: 使用手动提供的密钥加密任何文件格式
- **自定义后缀支持**: 可从 locked、enc 或 secret 后缀中选择
- **密码保护**: 文件使用密码保护进行加密
- **需要密钥**: 您必须提供密钥才能加密文件
- **灵活的文件支持**: 适用于任何文件类型

#### 通用加密 - 自动生成密钥
- **加密任何文件类型**: 使用自动生成的密钥加密任何文件格式
- **自定义后缀支持**: 可从 locked、enc 或 secret 后缀中选择
- **自动密钥生成**: 系统自动生成安全的密钥
- **密钥显示**: 加密后显示生成的密钥
- **保存您的密钥**: 重要：保存生成的密钥以便稍后打开文件
- **灵活的文件支持**: 适用于任何文件类型

### 4. 解密

#### 简单解密
- **解密 PDF、ZIP、7Z 文件**: 解密使用简单加密方法加密的 PDF、ZIP 或 7Z 文件
- **需要密钥**: 您必须提供加密时使用的密钥
- **自动文件类型检测**: 自动检测文件类型并输出正确格式
- **支持格式**: PDF、ZIP、7Z

#### 高级解密
- **解密任何加密文件**: 将带有 locked、enc 或 secret 后缀的文件解密为原始格式
- **需要密钥**: 您必须提供加密时使用的密钥
- **自动文件类型检测**: 自动检测原始文件类型并输出正确格式
- **灵活的文件支持**: 适用于任何加密文件

#### 通用解密
- **解密任何加密文件**: 将带有 .pdf.locked、.mp4.enc、.xlsx.secret 等后缀的文件解密为原始格式
- **需要密钥**: 您必须提供加密时使用的密钥
- **自动文件类型检测**: 自动检测原始文件类型并输出正确格式
- **灵活的文件支持**: 适用于任何加密文件

## 开发者信息

- **作者**: `https://github.com/sawyer-shi`
- **邮箱**: sawyer36@foxmail.com
- **许可证**: Apache License 2.0
- **源代码**: `https://github.com/sawyer-shi/dify-plugins-file_encrypt_decrypt`
- **支持**: 通过 Dify 平台和 GitHub Issues

## 许可证声明

本项目根据 Apache License 2.0 许可。有关完整的许可证文本，请参阅 [LICENSE](LICENSE) 文件。

---

**准备好在本地加密和解密您的文件了吗？**
