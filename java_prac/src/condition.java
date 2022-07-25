import java.util.Scanner;

public class condition {
    public static void main(String[] args) {
        System.out.println("This is the output from condition.java");
        if_condition();
        sanyuan();
        switch_fun();
        while_fun();
        do_while();
        for_loop();
        through();
        for_for();
        for_array();
        break_continue();
        scanner_break_continue();
    }

    /*
    * 条件判断语句
    */
    public static void if_condition() {
        int score = 80;
        int reward;
        if (score > 80){
            reward = score * 2;
        } else if(score > 60) {
            reward = score;
        } else {
            reward = 0;
        }

        System.out.println("Reward1: " + reward);
    }

    /*
    * 三元运算法判断
    */
    public static void sanyuan() {
        int score = 90;
        int reward = score > 80 ? score*2 : 0;
        System.out.println("Reward2: " + reward);
    }

    /*
    * switch
    */
    public static void switch_fun() {
        char grade = 'A';
        switch (grade){
            case 'A':
                System.out.println("You did a great job!");
                break;
            case 'B':
                System.out.println("You did a good job!");
                break;
            case 'C':
                System.out.println("You did it!");
                break;
            default:
                System.out.println("Meet you in the next year!");
        }
    }

    /*
    * while_func() while 循环
    */
    public static void while_fun() {
        int i = 0;
        while (i < 5){
            System.out.println(i);
            i++;
        }
    }

    /*
    * do_while() function
    */
    public static void do_while() {
        System.out.println("do_while() function");
        int i = 0;
        do{
            System.out.println(i);
            i++;
        }while (i<0);
    }

    /*
    * for_loop()
    */
    public static void for_loop() {
        System.out.println("For loop function:");
        for(int i = 0; i<5; i++) { //第一个condition只执行一次
            System.out.println(i);
        }
    }

    /*
    * 遍历数组 for loop
    */
    public static void through() {
        System.out.println("for loop 遍历数组");
        String[] names = {"Zoey", "Alex"};
        for (String name: names){
            System.out.println(name);
        }
    }

    /*
    * 嵌套循环
    */
    public static void for_for() {
        System.out.println("嵌套循环：");
        for (int i = 0; i <10; i++){
            for (int j = 0; j < 10; j++) {
                System.out.println(j*10+i);
            }
        }
    }

    /*
    * 遍历多维数组
    */
    public static void for_array() {
        System.out.println("遍历数组:");
        int[][] mat = {{1,2,3,4,5}, {9,8,7,6,5}};
        for (int i = 0; i < mat.length; i++){
            for (int j = 0; j < mat[i].length; j++){
                System.out.println(mat[i][j]);
            }
        }
    }

    /*
    * break_continue
    */
    public static void break_continue() {
        int[] nums = {1,9,30,99,0,3};
        System.out.println("The break loop: ");
        for (int num: nums){
            if (num > 30) {
                break;
            }
            System.out.println(num + " ");
        }
        System.out.println("The continue loop: ");
        for (int num: nums){
            if (num > 30){
                continue;
            }
            System.out.println(num + " ");
        }
    }

    /*
    * scanner
    */
    public static void scanner_break_continue() {

        // initialize hte input function to interact with the user
        Scanner input = new Scanner(System.in);
        // initialize the sum
        int sum = 0;

        // while loop
        while (true){
            System.out.println("===============\nPlease input an odd number:");
            // read the num
            int num = input.nextInt();
            // if the num is odd, add it to the sum
            if (num % 2 == 1){
                sum += num;
                System.out.println("Present value of sum:" + sum);
                continue;
            }
            // else continue to ask the user to continue or not
            input.nextLine();
            System.out.println("your number is not odd, do you want to continue? (Y/N)");
            String response = input.nextLine();
            if (response.toLowerCase().charAt(0) == 'n'){
                break;
            }
        }
        System.out.println("============\nThe total sum is: " + sum);
    }



}
