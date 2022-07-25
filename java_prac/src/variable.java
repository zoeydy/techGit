import static java.lang.System.out;

public class variable {
    public static void main(String[]args){
        //变量、常量、字面量

        //变量
        int intVar = 10;
        System.out.println("the value of variable intVar is: " + intVar);
        intVar = 20;
        System.out.println("the changed value of variable intVar is: " + intVar);

        //常量
        final int intFvar = 30;
        System.out.println("the value of F_variable is: " + intFvar);

        //赋值
        assignment();
        //数据转换
        convert();
        //数组
        array();
        //多位数组
        multi_array();
        //内置函数
        inbuid_fun();

    }

    /*
     * 赋值
     * */
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

    /*
     * 数据转换
     * */
    public static void convert(){
        //自动类型转换：小数据可以转换为大数据
        //byte -> short -> char -> int -> long -> float -> double
        short shortNum = 99;
        int intNum = shortNum;
        out.println("Convert short to int: " + intNum);

        double double_num = 9.999;
        float float_num = (float) double_num;
        short short_num = (short) double_num;
        out.println("Convert double(" + double_num + ") to float: " + float_num);
        out.println("Convert double(" + double_num + ") to short: " + short_num);
    }

    /*
     * 数组
     */
    public static void array() {
        int[] nums = {1,2,4,5,6,9};
        String[] names = {"Zoey", "Alex"};
        out.println("The 2ed elements of nums and names are: " + nums[1] + " and " + names[1]);

        nums[5] = 0;
        out.println("The changed 6th number of nums is: " + nums[5]);
    }

    /*
     * 多维数组
     */
    public static void multi_array() {
        int[][] mat = {{3,7,9},{2,3,6}};
        out.println("The number in the first row and second column of mat is " + mat[0][1]);
    }

    /*
     * 内置函数
     */
    public static void inbuid_fun() {
        String output = "Hello, world!";
        out.println(output.length());
        out.println(output.toUpperCase());
        out.println(output.indexOf("world"));

        //
        int[] nums = {1,2,3,4,5};
        out.println(Math.max(nums[1], 9));
        out.println(Math.random());
        out.println(Math.abs(-3));
        out.println(Math.sqrt(36));
    }
}

