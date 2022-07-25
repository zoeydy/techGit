import static java.lang.System.*;

public class Main  {
    public static void main(String[] args){
        out.println("hello, there are the presentation space!");
        assignment();
        convert();
    }
    public static void assignment() {

        //java 基本数据类型：byte1; short2; int4; long8; float4; double8; boolean1; char2

        //变量赋值格式: var_type variable = value;
        String name = "zoey";
        out.printf(name + "\n");

        int num = 3;
        out.printf("The value of variable num is: " + num);
        int num2 = 300;
        out.println("\nnum + num2 = " + (num2+num));
        out.println("num + num2 = " + num2+num);

        //创建常量
        final int num3 = 200;
        //num3 = 333; 会报错

    }

    public static void convert(){
        //自动类型转换：小数据可以转换为大数据
        //byte -> short -> char -> int -> long -> float -> double
        short shortNum = 99;
        int intNum = shortNum;
        out.println(intNum);

        String test = "abc";
    }

}
