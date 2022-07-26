import javax.smartcardio.CommandAPDU;
import java.util.Locale;
import java.util.TreeMap;

public class method {
    /*
     * 创建方法method（只能在类class里建立）
     * public static 是方法的修饰，表示其适用范围
     * void 表示返回值为空
     * 调用方法：方法名（）
     */
    public static void main(String[] args) {
        System.out.println("This is the main function: ");
        print_opposite_num(9);
        print_name("zoey", "dy");
        plus5(9);
        is_even(9);
        // 同样的方法名，不同的数据类型
        System.out.println("The sum function: \n" + sum(1,2) );
        method class4method = new method(); // 创建此时所在类的实例以使用sum method（which 未设置static修饰符 不是全局的方法）
        System.out.println(class4method.sum(1.1,1.3));
        //内置方法
        inbuild();
    }

    public static void print_opposite_num(int num) {
        System.out.println(0-num);
    }
    public static void print_name(String first_name, String last_name) {
        System.out.println(first_name + " " + last_name);
    }
    /*
    * 返回值
    */
    public static int plus5(int num) {
        System.out.println(num+5);
        return num+5;
    }
    public static boolean is_even(int num) {
        if (num%2==0){
            System.out.println("true");
            return true;
        } else {
            System.out.println("false");
            return false;
        }
    }

    public static int sum(int num1, int num2) {
        return num1 + num2;
    }
    public double sum(double num1, double num2) {
        return num1 + num2;
    }

    /*
    * java 内置方法
    */
    public static void inbuild() {
        String str = "    Hello, world    ";
        System.out.println(str);
        str = str.trim();
        System.out.println(str);
        str = str.replace("world", "zoey");
        System.out.println(str);
        str = str.substring(1,9);
        System.out.println(str);
        str = str.toUpperCase();
        System.out.println(str);
        char[] charArray = str.toCharArray();
        System.out.println(charArray);
    }


}
