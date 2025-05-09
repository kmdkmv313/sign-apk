import android.content.Context;
import android.content.res.AssetManager;
import android.util.Base64;

import java.io.InputStream;
import java.security.SecureRandom;
import javax.crypto.Cipher;
import javax.crypto.spec.IvParameterSpec;
import javax.crypto.spec.SecretKeySpec;
import java.io.ByteArrayOutputStream;

public class AssetDecryptor {

    private static final String SECRET_KEY = "ThisIsASecretKey";
    private static final String TRANSFORMATION = "AES/CBC/PKCS5Padding";

    public static byte[] decryptAsset(Context context, String assetFileName) {
        try {
            AssetManager assetManager = context.getAssets();
            InputStream inputStream = assetManager.open(assetFileName);

            byte[] fileData = readAllBytes(inputStream);

            IvParameterSpec iv = new IvParameterSpec(SECRET_KEY.getBytes("UTF-8"));
            SecretKeySpec keySpec = new SecretKeySpec(SECRET_KEY.getBytes("UTF-8"), "AES");

            Cipher cipher = Cipher.getInstance(TRANSFORMATION);
            cipher.init(Cipher.DECRYPT_MODE, keySpec, iv);

            return cipher.doFinal(fileData);

        } catch (Exception e) {
            e.printStackTrace();
            return null;
        }
    }

    private static byte[] readAllBytes(InputStream inputStream) throws Exception {
        ByteArrayOutputStream buffer = new ByteArrayOutputStream();
        int nRead;
        byte[] data = new byte[4096];
        while ((nRead = inputStream.read(data, 0, data.length)) != -1) {
            buffer.write(data, 0, nRead);
        }
        buffer.flush();
        return buffer.toByteArray();
    }
}
