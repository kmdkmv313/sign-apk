import os
import shutil
import zipfile
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
from base64 import b64encode

KEY = b'ThisIsASecretKey'
BLOCK_SIZE = 16

def encrypt_file(filepath):
    with open(filepath, 'rb') as f:
        data = f.read()

    cipher = AES.new(KEY, AES.MODE_CBC, iv=KEY)
    encrypted = cipher.encrypt(pad(data, BLOCK_SIZE))

    with open(filepath, 'wb') as f:
        f.write(encrypted)

def unzip_apk(apk_path, output_dir):
    with zipfile.ZipFile(apk_path, 'r') as zip_ref:
        zip_ref.extractall(output_dir)

def zip_apk(folder_path, output_apk):
    with zipfile.ZipFile(output_apk, 'w') as zipf:
        for root, dirs, files in os.walk(folder_path):
            for file in files:
                full_path = os.path.join(root, file)
                arcname = os.path.relpath(full_path, folder_path)
                zipf.write(full_path, arcname)

def encrypt_assets(apk_path):
    temp_dir = 'apk_temp'
    encrypted_apk = 'encrypted_output.apk'

    if os.path.exists(temp_dir):
        shutil.rmtree(temp_dir)
    os.makedirs(temp_dir)

    unzip_apk(apk_path, temp_dir)

    asset_dir = os.path.join(temp_dir, 'assets')
    if not os.path.exists(asset_dir):
        print("[!] لا يوجد مجلد assets داخل الـ APK.")
        return

    for root, dirs, files in os.walk(asset_dir):
        for file in files:
            filepath = os.path.join(root, file)
            encrypt_file(filepath)
            print(f"[+] تم تشفير: {filepath}")

    zip_apk(temp_dir, encrypted_apk)
    print(f"[✓] APK المشفر: {encrypted_apk}")
    print("[!] يجب توقيع الـ APK يدويًا قبل التثبيت.")

if __name__ == "__main__":
    original_apk = "your_app.apk"
    encrypt_assets(original_apk)
