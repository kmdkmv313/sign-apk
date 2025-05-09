# 🔐 APK Asset Encryptor

أداة Python لتشفير ملفات `assets/` داخل ملفات APK باستخدام AES، مع كود Java لفك التشفير داخل تطبيق Android (يدعم Android 14).

## ✅ الوظائف
- فك ضغط ملف APK
- تشفير الملفات داخل مجلد `assets/` باستخدام AES
- إعادة حزم الملف APK (يحتاج توقيع خارجي)
- مثال كود Java لفك التشفير في وقت التشغيل

## 🔧 المتطلبات
- Python 3
- مكتبة pycryptodome
- أدوات Android SDK: zipalign, apksigner

## 🛠️ طريقة الاستخدام

```bash
python encrypt_apk_assets.py
```

ثم وقّع الملف يدويًا:

```bash
zipalign -v 4 encrypted_output.apk aligned.apk
apksigner sign --ks my-release-key.jks --out signed.apk aligned.apk
```

## 🔓 كود فك التشفير (Java)

الموجود داخل مجلد `decryptor/`

## ⚠️ ملاحظات أمنية
- المفتاح مشفر بشكل ثابت لأغراض تعليمية فقط
- في البيئات الحقيقية، استخدم KeyStore أو Native Layer

## 📄 الترخيص
MIT License – مفتوح المصدر للاستخدامات القانونية والتعلم فقط.
