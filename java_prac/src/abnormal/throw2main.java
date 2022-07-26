package abnormal;

import java.util.logging.FileHandler;

public class throw2main {
    public static void main(String[] args) {
        try {
            bad_code(17);
        } catch (Exception error){
            System.out.println(error);
        } finally {
            System.out.println("finally");
        }
    }

    public static void bad_code(int age) throws Exception{
        if (age < 18) {
            throw new Exception("You are not old enough");
        } else {
            System.out.println("welcome to the star bar!");
        }
    }
}
