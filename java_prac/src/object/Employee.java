package object;

// 创建类
public class Employee {


    public static void main(String[] args) {
        // 创建实例
        Employee employee1 = new Employee("employee1");
        Employee employee2 = new Employee();

        // 调用实例方法
        System.out.println(employee1.name);
        employee1.getSalary();
        System.out.println(employee2.name);
        employee2.quit();
    }

    // 初始化参数值：构建函数
    // 初始化不同个数的参数（在括号中声明要初始化的参数）
    public Employee(){
        name = "default name";
        salary = 500000;
    }
    public Employee(String name){
        name = "default name 2";
    }

    // 申明参数（默认值）
    // String name = "cole";
    //int salary = 100000;
    int salary;
    String name;
    // 创建方法
    public int getSalary(){
        System.out.println(salary);
        return salary;
    }
    public void quit(){
        System.out.println("I'm out!");
    }

    //修饰符：public private
    void greet() {
        System.out.println("Hey, this is the greet from method decorated by void. ");
    }
}
