package file;

import java.io.File;
import java.io.IOException;

public class build {
    public static void main(String[] args) {
        File new_file = new File("new_file.txt");
        try {
            if (new_file.createNewFile()) {
                System.out.println(new_file.getName() + "created.");
            } else {
                System.out.println("File ia already existed.");
            }
        } catch (IOException error) {
            System.out.println("An error happened: ");
            error.printStackTrace();
        }
    }
}
