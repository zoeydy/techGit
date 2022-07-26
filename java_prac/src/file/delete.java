package file;

import java.io.File;

public class delete {
    public static void main(String[] args) {
        File my_file = new File("new_file.txt");
        if (my_file.delete()) {
            System.out.println("Successful deleted the file: " + my_file.getName());
        } else {
            System.out.println("Fail to delete the file: " + my_file.getName());
        }
    }
}
