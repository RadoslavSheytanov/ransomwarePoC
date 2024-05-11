# Ransomware Sample written in Python - Proof Of Concept Implementation

**DISCLAIMER: The use of this script for any malicious or illegal activities is strictly prohibited. Radoslav, the author of this script shall not be held responsible for any damages or legal consequences resulting from its misuse. Always use this script in a legal and ethical manner, respecting the privacy and rights of others.**

## Overview
This Python script implements a simple ransomware application that encrypts files within specified directories using the AES encryption algorithm. It also includes functionality for decrypting files upon successful payment verification. This ransomware as mentioned above is provided for educational purposes only. Radoslav is not responsible for any misuse of the provided malware sample

## Features
1. **Encryption**: Files within specified directories are encrypted using AES encryption with Cipher Block Chaining (CBC) mode.
2. **Decryption**: Decryption of encrypted files is possible upon successful payment verification using a hardcoded key.
3. **Ransom Note**: A ransom note is generated and placed in the directory to notify the user of the encryption and payment instructions.
4. **Lock System**: The script includes a feature to lock the system after encryption, implemented using a Visual Basic Script (VBS) file.

## Dependencies
- **Python 3.x**: The script is written in Python and requires Python 3.x to run.
- **pycryptodome**: This library is used for AES encryption and decryption. Install it using `pip install pycryptodome`.

## Usage
1. **Encryption**: Run the script to encrypt files within specified directories. Update the `directories_to_encrypt` variable with the desired directories.
2. **Decryption**: Decrypt files after successful payment verification by setting the `ransom_key` variable to the correct verification key and running the script.
3. **Ransom Note**: A ransom note (`README_TO_DECRYPT.txt`) is generated in the encrypted directories with payment instructions.
4. **Lock System**: The `lock_system` function locks the system after encryption using a VBS script (`lock.vbs`).

## Security Considerations
- **Hardcoded Key**: The script uses a hardcoded key for decryption, which should be securely stored and only provided upon successful payment verification.
- **File Integrity**: Ensure that encrypted files are not modified or tampered with during transmission or decryption to prevent data corruption.
- **System Lock**: Use the system lock feature with caution, as it may cause inconvenience to users if triggered unintentionally.

## Disclaimer
This script is provided for educational purposes only. Unauthorized use of ransomware techniques for malicious purposes is illegal and unethical. Use responsibly and ensure compliance with applicable laws and regulations.

**DISCLAIMER: The use of this script for any malicious or illegal activities is strictly prohibited. Radoslav, the author of this script shall not be held responsible for any damages or legal consequences resulting from its misuse. Always use this script in a legal and ethical manner, respecting the privacy and rights of others.**
