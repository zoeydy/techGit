package file;

import java.io.File;

public class info {
    public static void main(String[] args) {
        File my_file = new File("new_file.txt");
        if (my_file.exists()){
            System.out.println("File name: " + my_file.getName());
            System.out.println("File absolute path: " + my_file.getAbsolutePath());
            System.out.println("File writable: " + my_file.canWrite());
            System.out.println("File readable: " + my_file.canRead());
            System.out.println("File size in bytes: " + my_file.length());
        } else {
            System.out.println("The file doesn't exist.");
        }
    }
}
