import java.util.HashMap;
import java.util.Map;
class Product {
    private String name;
    private int quantity;
    private double price;
    public Product(String name, int quantity, double price) {
        this.name = name;
        this.quantity = quantity;
        this.price = price;
    }
    @Override
    public String toString() {
        return name + " (Qty: " + quantity + ", Price: $" + price + ")";
    }
    public void updateQuantity(int soldQuantity) {
        if (quantity >= soldQuantity) {
            quantity -= soldQuantity;
            System.out.println("Updated quantity for " + name + ": " + quantity);
        } else {
            System.out.println("Insufficient stock for " + name);
        }
    }
    public static void main(String[] args) {
        Product product1 = new Product("Widget", 100, 10.0);
        Product product2 = new Product("Gadget", 50, 20.0);
        product1.updateQuantity(20);
        product2.updateQuantity(60);
        System.out.println(product1);
        System.out.println(product2);
    }
}
