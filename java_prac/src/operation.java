//运算符： + - * / % ++ --

import sun.lwawt.macosx.CPrinterDevice;

import javax.swing.*;

import static java.lang.System.out;

public class operation {
    public static void main(String[] args) {
        // 算术运算符
        operation.testOper();
        //关系运算符：== != > < >= <=
        testRelation(); //因为都是静态功能所以可以直接在类里直接调用
        //位运算符
        operation();
        //赋值运算符
        //其他运算符
        //条件运算符
        testCondition();
    }
    public static void testOper(){

        // basic arithmetic operations
        int a = 10;
        int b = 20;
        int c;
        c = a + b;

        System.out.println(a - b);
        System.out.println(c);

        //模的运算
        int d = 12 % 5;
        System.out.println(d);

        // 区分前缀后缀
        a++;
        System.out.println(a);
        ++a;
        System.out.println(a);

        int m = 10;
        int n = 10;
        System.out.println("2 * m++ = " + 2 * m++);
        System.out.println("2 * ++n = " + 2 * ++n);
    }

    public static void testRelation(){
        int a = 10;
        int b = 10;
        int c = 15;
        System.out.println("bool test: " + (a == b));
        System.out.println("bool test: " + (a == c));
    }

    public static void testCondition(){
        int a, b;
        a = 10;
        b = (a == 10) ?20 :30; //(条件判断) ？为真时 ：为假时
        System.out.println("The condition test: " + b);
    }

    /*
     * 操作符 运算符(加减乘除，取余%，num++，关系运算符, 位运算符)
     * 位运算符：e.g. (5 = *101； 3 = *011) -> (5+3 = *101+*011 = *1000)
     * 逻辑运算符： &&, ||, !
     * 条件运算符 (三元运算符)
     * */
    public static void operation() {
        int num1 = 5; //(101)
        int num2 = 3;
        out.println(num1 > num2);
        out.println(num1 == num2);
        out.println(~num1);
        out.println(num1 <<= 1);
        out.println(num1 >>= 2);

        // 条件运算符
        boolean flag = true;
        int num = !flag ? 100:-100;
        out.println("条件运算符：\n" + num);
    }
}