import java.io.*;
import javax.crypto.*;
import javax.crypto.spec.*;
import java.security.spec.*;

public class decryptFile {

    public static void main(String[] args) {

        try {

            if (args.length != 3) {
                System.out.println("Usage: java decryptFile <file> <DES|3DES> <password>");
                return;
            }

            String inputFile = args[0];
            String algorithm = args[1];
            String password = args[2];

            // Convert 3DES name
            if (algorithm.equalsIgnoreCase("3DES")) {
                algorithm = "PBEWithMD5AndTripleDES";
            } else {
                algorithm = "PBEWithMD5AndDES";
            }

            // Output file name (remove .encrypted if possible)
            String outputFile = inputFile.replace(".encrypted", "") + ".decrypted";

            byte[] iv = new byte[]{
                (byte)0x8E, (byte)0x12, (byte)0x39, (byte)0x9C,
                (byte)0x07, (byte)0x72, (byte)0x6F, (byte)0x5A
            };

            int iterationCount = 19;

            AlgorithmParameterSpec paramSpec = new PBEParameterSpec(iv, iterationCount);
            KeySpec keySpec = new PBEKeySpec(password.toCharArray(), iv, iterationCount);

            SecretKey key = SecretKeyFactory.getInstance(algorithm).generateSecret(keySpec);

            Cipher dcipher = Cipher.getInstance(key.getAlgorithm());
            dcipher.init(Cipher.DECRYPT_MODE, key, paramSpec);

            FileInputStream fis = new FileInputStream(inputFile);
            CipherInputStream cis = new CipherInputStream(fis, dcipher);
            FileOutputStream fos = new FileOutputStream(outputFile);

            byte[] buffer = new byte[1024];
            int bytesRead;

            while ((bytesRead = cis.read(buffer)) != -1) {
                fos.write(buffer, 0, bytesRead);
            }

            cis.close();
            fos.close();

            System.out.println("Decrypted file created: " + outputFile);

        } catch (Exception e) {
            System.out.println("Error: " + e);
        }
    }
}