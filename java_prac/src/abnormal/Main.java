package abnormal;

public class Main {
    public static void main(String[] args) {
        try {
            System.out.println(1/0);
            int[] array = {1,2,3};
            System.out.println(array[3]);
        } catch (Exception error) {
            System.out.println(error);
        } catch (OutOfMemoryError error) {
            System.out.println(error);
        } finally {
            System.out.println("Finally");
        }
    }
}
