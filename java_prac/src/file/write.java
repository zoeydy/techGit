package file;

import java.io.File;
import java.io.FileWriter;
import java.io.IOException;
import java.util.logging.FileHandler;

public class write {
    public static void main(String[] args) {
        try {
            FileWriter write_file = new FileWriter("new_file.txt");
            write_file.write("Hello, world! \nThis is the second line,");
            write_file.close();
        } catch (Exception error) {
            System.out.println("An error happend: ");
            error.printStackTrace();
        }
    }
}
