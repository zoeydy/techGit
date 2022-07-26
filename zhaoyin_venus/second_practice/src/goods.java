public class goods {

    public static void main(String[] args) {
        System.out.println("This is the information of the good: ");
    }

    int id;
    int stock;
    String info;
    int price;

    // 初始化商品信息
    public goods(){
        id = 1;
        stock = 10000;
        info = "This is the info of the good";
        price = 9;
    }

    public int getId() {
        return id;
    }
    public int getPrice() {
        return price;
    }
    public int getStock() {
        return stock;
    }
    public String getInfo() {
        return info;
    }
}
