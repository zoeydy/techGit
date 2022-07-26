package file;

import java.io.File;
import java.io.FileNotFoundException;
import java.io.IOException;
import java.util.Scanner;

public class read {
    public static void main(String[] args) {
        try {
            File my_file = new File("new_file.txt");
            Scanner reader = new Scanner(my_file);
            while (reader.hasNextLine()) {
                System.out.println(reader.nextLine());
            }
            reader.close();
        } catch (FileNotFoundException error) {
            System.out.println(error);
            error.printStackTrace();
        }
    }
}
