// 数据类型（基本+引用）

public class datatype {
    public static void main(String[] args) {

        /*
         * 基本数据类型：
         * byte 字节型 1
         * short 短整型 2
         * int 整型 4
         * long 长整型 8
         * float 单精度 4
         * double 双精度 8
         * char 字符型 1
         * boolean 布尔型 1或4
         */
        byte byteVar = 15;
        short shortVar = 12345;
        int intVar = 100000;
        long longVar = 1000000000L; // L 可大写也可小写

        float fVar = 1.23f;
        double dVar = 1.23;

        char ch01 = 'a';
        char ch02 = '谁';
        // char fals = '你是谁？'；
        String str01 = "你是谁？";

        boolean boo = false;
        boolean test = Boolean.parseBoolean("there is something");

        System.out.println(byteVar);
        System.out.println(shortVar);
        System.out.println(intVar);
        System.out.println(longVar);
        System.out.println(fVar);
        System.out.println(dVar);
        System.out.println(ch01);
        System.out.println(ch02);
        System.out.println(str01);
        System.out.println(boo);
        System.out.println(test);

        /* 引用（复合）数据类型
        类 class； 接口 interfa； 数组
        */

    }
}