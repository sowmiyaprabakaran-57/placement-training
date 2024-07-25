class Item {
    private String name;
    private int quantity;
    private double price;

    public Item(String name, int quantity, double price) {
        this.name = name;
        this.quantity = quantity;
        this.price = price;
    }

    public double getTotalCost() {
        return quantity * price;
    }
}

class ShoppingCart {
    private List<Item> items = new ArrayList<>();

    public void addItem(Item item) {
        items.add(item);
    }

    public double calculateTotalCost() {
        double total = 0;
        for (Item item : items) {
            total += item.getTotalCost();
        }
        return total;
    }
}

public class OnlineShoppingCartExample {
    public static void main(String[] args) {
        Item item1 = new Item("Shirt", 2, 25.0);
        Item item2 = new Item("Jeans", 1, 50.0);

        ShoppingCart cart = new ShoppingCart();
        cart.addItem(item1);
        cart.addItem(item2);

        System.out.println("Total cost: $" + cart.calculateTotalCost());
    }
}
