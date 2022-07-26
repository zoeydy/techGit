package abnormal;

import java.awt.image.ComponentColorModel;
import java.io.CharArrayReader;

public class throws2main {
    public static void main(String[] args) {
        try {
            bad_code();
        } catch (Exception error) {
            System.out.println(error);
        } finally {
            System.out.println("Finally");
        }
    }

    public static void bad_code() throws Exception {
        int[] array = {1,2,3};
        System.out.println(array[3]);
    }
}
