
📝 محتوى محدث لـ README.md
markdown
نسخ
تحرير
# 🔐 APK Asset Encryptor

أداة Python لتشفير ملفات `assets/` داخل ملفات APK باستخدام AES، مع كود Java لفك التشفير داخل تطبيق Android (يدعم Android 14). تشمل الأداة دعمًا لتوقيع APK تلقائيًا باستخدام GitHub Actions.

---

## ✅ الميزات

- فك ضغط ملف APK
- تشفير ملفات داخل `assets/` باستخدام AES CBC
- إعادة إنشاء APK محمي
- كود Java لفك التشفير في وقت التشغيل
- توقيع APK تلقائيًا عبر GitHub Actions

---

## 🔧 المتطلبات

- Python 3
- مكتبة [`pycryptodome`](https://pypi.org/project/pycryptodome/)
- Android SDK Tools: `zipalign`, `apksigner`

```bash
pip install pycryptodome
🛠️ الاستخدام المحلي
شغّل أداة التشفير:

bash
نسخ
تحرير
python encrypt_apk_assets.py
وقّع ملف encrypted_output.apk يدويًا (اختياري):

bash
نسخ
تحرير
zipalign -v 4 encrypted_output.apk aligned.apk
apksigner sign --ks my-release-key.jks --out signed.apk aligned.apk
🔐 التوقيع التلقائي عبر GitHub Actions
📁 ملف العمل:
.github/workflows/sign-apk.yml

📤 ماذا يفعل:
عند رفع ملف encrypted_output.apk إلى GitHub، يقوم بـ:

استخراج keystore من Secret

توقيع الملف باستخدام apksigner

رفع signed.apk كـ Artifact تلقائي

🧾 المتطلبات (GitHub Secrets):
Secret Name	القيمة
KEYSTORE_B64	مفتاح JKS مشفر بصيغة base64
KEYSTORE_PASSWORD	كلمة المرور للـ keystore
KEY_ALIAS	الاسم المستخدم داخل keystore
KEY_PASSWORD	كلمة المرور للمفتاح

⚠️ لا ترفع المفتاح نفسه علنًا أبدًا – استخدم Secrets فقط.

🔓 كود فك التشفير (Java)
موجود داخل مجلد decryptor/:

AssetDecryptor.java

example_usage.java
