public class Main {
    public static void main(String[] args) {
        goods good1 = new goods();
        System.out.println("商品ID:" + good1.getId());
        System.out.println("商品价格:" + good1.getPrice());
        System.out.println("商品库存:" + good1.getStock());
        System.out.println("商品信息:" + good1.getInfo());
        //用户输入购买商品id
            //积分不足：返回错误信息

            //积分充足
                // 库存不足：返回错误信息
                // 库存充足：扣除积分，扣减库存，更新订单

    }







}