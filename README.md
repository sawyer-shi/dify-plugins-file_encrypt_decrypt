# File Encrypt & Decrypt

A powerful Dify plugin providing comprehensive **local** file encryption and decryption capabilities. All file operations are executed entirely on your local machine without any external services, API keys, or internet connections, ensuring maximum data security and privacy. Supports encryption and decryption of various file formats with customizable encryption suffixes.

Supported file types include: .pdf, .txt, .doc, .docx, .xls, .xlsx, .ppt, .pptx, .rtf, .odt, .ods, .odp, .md, .csv, .html, .htm, .css, .js, .json, .xml, .py, .java, .c, .cpp, .h, .hpp, .cs, .php, .rb, .go, .rs, .swift, .kt, .ts, .tsx, .jsx, .vue, .sql, .jpg, .jpeg, .png, .gif, .bmp, .svg, .tiff, .ico, .webp, .mp3, .wav, .ogg, .mp4, .avi, .mov, .wmv, .flv, .mkv, .webm, .zip, .7z, .tar, .gz, .bz2, .xz, .rar, .iso, .dmg, .exe, .msi, .apk, .ipa, .deb, .rpm, .sh, .bat, .ps1, .dll, .so, .dylib, .lib, .a, .o, .class, .jar, .war, .ear, .swf, .fla, .as, .mxp, .air, .zxp, .pem, .crt, .cer, .der, .p12, .pfx, .key, .pub, .asc, .sig, .gpg, .p7s, .p7b, .p7r, .p7c, .spc, .sst, .stl, .pko, .cat, .crl, .rl, .wrl, .vrm, .vrml, .igs, .iges, .msh, .mesh, .silo, .obj, .mtl, .stl, .dxf, .dwg, .dwf, .gbr, .gtl, .gbl, .gbo, .gbs, .gml, .gko, .gm1, .gm2, .gm3, .cmp, .sol, .stc, .sts, .plc, .top, .drd, .art, .rep, and many more....

## Version Information

- **Current Version**: v0.0.2
- **Release Date**: 2026-01-16
- **Compatibility**: Dify Plugin Framework
- **Python Version**: 3.12

### Version History
- **v0.0.2** (2026-01-16): Update plugin description and optimize file type descriptions
- **v0.0.1** (2026-01-14): Initial version with file encryption and decryption features

## Quick Start

1. Download the file_encrypt_decrypt plugin from Dify marketplace
2. Install the plugin in your Dify environment
3. Start encrypting and decrypting your files immediately

## Core Features
<img width="733" height="1718" alt="English" src="https://github.com/user-attachments/assets/453d2414-64b1-4cc0-bbce-e99966e6619a" /><img width="748" height="1656" alt="Chinese" src="https://github.com/user-attachments/assets/9cadfcb7-a581-4477-b34b-808325ee330d" />


- **100% Local Processing**: All file encryption and decryption operations are executed entirely on your local machine
- **No External Services**: No need to connect to any external services or third-party APIs
- **No API Keys Required**: Completely free to use without any API key configuration
- **Maximum Data Security**: Your files never leave your local environment, ensuring complete privacy and security
- **Zero Network Dependency**: Works offline without internet connection
- **Customizable Encryption Suffixes**: Choose from locked, enc, or secret suffixes for encrypted files
- **Flexible Key Management**: Support for both manual key input and auto-generated keys

## Technical Advantages

- **Local Processing**: All file encryption and decryption is executed locally without external dependencies
- **High Security**: Uses strong encryption algorithms to protect your files
- **Flexible Options**: Various configuration options for different use cases
- **Error Handling**: Robust error handling with informative messages
- **Secure Processing**: Files are processed securely without data retention
- **Customizable Suffixes**: Choose encryption suffixes to organize encrypted files

## Requirements

- Python 3.12
- Dify platform access
- Required Python packages (install via requirements.txt)


## Usage

If you want to add other file types in Dify, please add all the file types you need:
<img width="1508" height="1874" alt="file-type" src="https://github.com/user-attachments/assets/afb3b41f-b97d-4d20-8b92-3b9e47337e89" />


The plugin provides the following tools:

### 1. Encrypt File Simple -- Manual Key (encrypt_file_simple_manual)
Encrypt PDF, ZIP, or 7Z files with a manually provided key.
- **Parameters**:
  - `file`: The file to encrypt (required)
  - `key`: The encryption key (required)
- **Features**:
  - Supports PDF, ZIP, 7Z files
  - Manual key input
  - Password protection
  - Displays file size and type
  - Outputs encrypted file
<img width="2156" height="1303" alt="simple-A-01" src="https://github.com/user-attachments/assets/9bf00078-7d63-4468-9894-f9c1a48ed301" />

### 2. Encrypt File Simple -- Auto Key (encrypt_file_simple_auto)
Encrypt PDF, ZIP, or 7Z files with an automatically generated key.
- **Parameters**:
  - `file`: The file to encrypt (required)
- **Features**:
  - Supports PDF, ZIP, 7Z files
  - Auto-generated key
  - Key displayed after encryption
  - Password protection
  - Displays file size and type
  - Outputs encrypted file
<img width="2256" height="1273" alt="simple-B-01" src="https://github.com/user-attachments/assets/ca2352ea-c581-4dcf-a1cc-93bc61e15d74" />

### 3. Decrypt File Simple (decrypt_file_simple)
Decrypt PDF, ZIP, or 7Z files that were encrypted with the simple encryption method.
- **Parameters**:
  - `file`: The encrypted file to decrypt (required)
  - `key`: The decryption key (required)
- **Features**:
  - Supports PDF, ZIP, 7Z files
  - Key required
  - Automatic file type detection
  - Outputs correct file type
  - Displays file size and type
<img width="2513" height="1388" alt="simple-C-01" src="https://github.com/user-attachments/assets/67c964d8-b1c9-445c-9116-517b499a06b7" />
<img width="791" height="375" alt="simple-C-02" src="https://github.com/user-attachments/assets/ebbc8e02-7037-4fe3-b02e-d913b6a27641" />
<img width="2524" height="1309" alt="simple-C-03" src="https://github.com/user-attachments/assets/3c72fa50-dccd-4f2a-a4fb-500af434b7ba" />

### 4. Encrypt File Normal -- Manual Key (encrypt_file_manual)
Encrypt any file type with a manually provided key and custom suffix.
- **Parameters**:
  - `file`: The file to encrypt (required)
  - `key`: The encryption key (required)
  - `suffix`: The encryption suffix (optional, default: locked)
    - `locked`: .locked suffix
    - `enc`: .enc suffix
    - `secret`: .secret suffix
- **Features**:
  - Supports any file type
  - Manual key input
  - Custom suffix selection
  - Password protection
  - Displays file size and type
  - Outputs encrypted file with custom suffix
<img width="2645" height="964" alt="normal-A-01" src="https://github.com/user-attachments/assets/f6860cb9-0cf4-4fb1-aa3a-cc0c0a9858a0" />


### 5. Encrypt File Normal -- Auto-generated Key (encrypt_file_auto)
Encrypt any file type with an automatically generated key and custom suffix.
- **Parameters**:
  - `file`: The file to encrypt (required)
  - `suffix`: The encryption suffix (optional, default: locked)
    - `locked`: .locked suffix
    - `enc`: .enc suffix
    - `secret`: .secret suffix
- **Features**:
  - Supports any file type
  - Auto-generated key
  - Key displayed after encryption
  - Custom suffix selection
  - Password protection
  - Displays file size and type
  - Outputs encrypted file with custom suffix
  <img width="2349" height="1165" alt="normal-B-01" src="https://github.com/user-attachments/assets/2382469f-b0b1-47a0-adcf-07669b38a057" />


### 6. Decrypt File Normal (decrypt_file)
Decrypt files with suffixes like .pdf.locked, .mp4.enc, .xlsx.secret into their original formats.
- **Parameters**:
  - `file`: The encrypted file to decrypt (required)
  - `key`: The decryption key (required)
- **Features**:
  - Supports any encrypted file
  - Key required
  - Automatic file type detection
  - Outputs correct file type
  - Displays file size and type
  <img width="2584" height="1606" alt="normal-C-01" src="https://github.com/user-attachments/assets/313cbf73-6f3d-4d92-bb26-bae9be5e76fc" />
<img width="2442" height="1468" alt="normal-C-02" src="https://github.com/user-attachments/assets/3d83d307-5003-46e8-9459-faa87c34981d" />


### 7. Encrypt File Pro -- Manual Key (encrypt_file_pro_manual)
Encrypt any file type with a manually provided key and custom suffix.
- **Parameters**:
  - `file`: The file to encrypt (required)
  - `key`: The encryption key (required)
  - `suffix`: The encryption suffix (optional, default: locked)
    - `locked`: .locked suffix
    - `enc`: .enc suffix
    - `secret`: .secret suffix
- **Features**:
  - Supports any file type
  - Manual key input
  - Custom suffix selection
  - Password protection
  - Displays file size and type
  - Outputs encrypted file with custom suffix
  <img width="2330" height="1061" alt="pro-A-01" src="https://github.com/user-attachments/assets/3db1441d-cc4d-428e-84af-5cf835b9b037" />


### 8. Encrypt File Pro -- Auto Key (encrypt_file_pro_auto)
Encrypt any file type with an automatically generated key and custom suffix.
- **Parameters**:
  - `file`: The file to encrypt (required)
  - `suffix`: The encryption suffix (optional, default: locked)
    - `locked`: .locked suffix
    - `enc`: .enc suffix
    - `secret`: .secret suffix
- **Features**:
  - Supports any file type
  - Auto-generated key
  - Key displayed after encryption
  - Custom suffix selection
  - Password protection
  - Displays file size and type
  - Outputs encrypted file with custom suffix
  <img width="2351" height="1234" alt="pro-B-01" src="https://github.com/user-attachments/assets/327f0df5-dc8d-42d0-8d37-ed45d75aa771" />

### 9. Decrypt File Pro (decrypt_file_pro)
Decrypt files with locked, enc, or secret suffixes into their original formats.
- **Parameters**:
  - `file`: The encrypted file to decrypt (required)
  - `key`: The decryption key (required)
- **Features**:
  - Supports any encrypted file
  - Key required
  - Automatic file type detection
  - Outputs correct file type
  - Displays file size and type
<img width="2378" height="1095" alt="pro-C-01" src="https://github.com/user-attachments/assets/18e4c481-8cfd-4006-9a49-dec7884e17f2" />
<img width="2448" height="1642" alt="pro-C-02" src="https://github.com/user-attachments/assets/e8c70a9c-0039-40a3-8243-d36dcc26b195" />



  
## Notes

- All file encryption and decryption is executed locally without uploading files to external services
- For auto-generated keys, make sure to save the key as it will be needed for decryption
- The same key must be used for encryption and decryption
- Simple encryption only supports PDF, ZIP, and 7Z files
- Pro and Normal encryption support any file type
- Encrypted files will have the selected suffix (locked, enc, or secret) appended
- Large files may require longer processing time depending on their size


## Core Functions

### 1. Simple Encryption

#### Simple Encryption with Manual Key
- **Encrypt PDF, ZIP, 7Z Files**: Encrypt PDF, ZIP, or 7Z files with a manually provided key
- **Password Protection**: Files are encrypted with password protection
- **Key Required**: You must provide a key to encrypt the file
- **Supported Formats**: PDF, ZIP, 7Z

#### Simple Encryption with Auto-generated Key
- **Encrypt PDF, ZIP, 7Z Files**: Encrypt PDF, ZIP, or 7Z files with an automatically generated key
- **Auto Key Generation**: System automatically generates a secure key
- **Key Display**: The generated key is displayed after encryption
- **Save Your Key**: Important to save the generated key to open the file later
- **Supported Formats**: PDF, ZIP, 7Z

### 2. Pro Encryption

#### Pro Encryption with Manual Key
- **Encrypt Any File Type**: Encrypt any file format with a manually provided key
- **Custom Suffix Support**: Choose from locked, enc, or secret suffixes
- **Password Protection**: Files are encrypted with password protection
- **Key Required**: You must provide a key to encrypt the file
- **Flexible File Support**: Works with any file type

#### Pro Encryption with Auto-generated Key
- **Encrypt Any File Type**: Encrypt any file format with an automatically generated key
- **Custom Suffix Support**: Choose from locked, enc, or secret suffixes
- **Auto Key Generation**: System automatically generates a secure key
- **Key Display**: The generated key is displayed after encryption
- **Save Your Key**: Important to save the generated key to open the file later
- **Flexible File Support**: Works with any file type

### 3. Normal Encryption

#### Normal Encryption with Manual Key
- **Encrypt Any File Type**: Encrypt any file format with a manually provided key
- **Custom Suffix Support**: Choose from locked, enc, or secret suffixes
- **Password Protection**: Files are encrypted with password protection
- **Key Required**: You must provide a key to encrypt the file
- **Flexible File Support**: Works with any file type

#### Normal Encryption with Auto-generated Key
- **Encrypt Any File Type**: Encrypt any file format with an automatically generated key
- **Custom Suffix Support**: Choose from locked, enc, or secret suffixes
- **Auto Key Generation**: System automatically generates a secure key
- **Key Display**: The generated key is displayed after encryption
- **Save Your Key**: Important to save the generated key to open the file later
- **Flexible File Support**: Works with any file type

### 4. Decryption

#### Simple Decryption
- **Decrypt PDF, ZIP, 7Z Files**: Decrypt PDF, ZIP, or 7Z files that were encrypted with the simple encryption method
- **Key Required**: You must provide the key used during encryption
- **Automatic File Type Detection**: Automatically detects file type and outputs correct format
- **Supported Formats**: PDF, ZIP, 7Z

#### Pro Decryption
- **Decrypt Any Encrypted File**: Decrypt files with locked, enc, or secret suffixes into their original formats
- **Key Required**: You must provide the key used during encryption
- **Automatic File Type Detection**: Automatically detects original file type and outputs correct format
- **Flexible File Support**: Works with any encrypted file

#### Normal Decryption
- **Decrypt Any Encrypted File**: Decrypt files with suffixes like .pdf.locked, .mp4.enc, .xlsx.secret into their original formats
- **Key Required**: You must provide the key used during encryption
- **Automatic File Type Detection**: Automatically detects original file type and outputs correct format
- **Flexible File Support**: Works with any encrypted file

## Developer Information

- **Author**: `https://github.com/sawyer-shi`
- **Email**: sawyer36@foxmail.com
- **License**: Apache License 2.0
- **Source Code**: `https://github.com/sawyer-shi/dify-plugins-file_encrypt_decrypt`
- **Support**: Available through Dify platform and GitHub Issues

## License Statement

This project is licensed under the Apache License 2.0. The full license text is available in the [LICENSE](LICENSE) file.

---

**Ready to encrypt and decrypt your files?**
