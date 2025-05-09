byte[] decryptedData = AssetDecryptor.decryptAsset(this, "config.json");
if (decryptedData != null) {
    String jsonString = new String(decryptedData, StandardCharsets.UTF_8);
    Log.d("Decrypted", jsonString);
}
