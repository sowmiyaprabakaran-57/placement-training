#include <stdio.h>
#include <stdlib.h>
struct Item {
    char name[50];
    int quantity;
    double price;
};
struct ShoppingCart {
    struct Item items[10];
    int itemCount;
};
void addItem(struct ShoppingCart *cart, struct Item item) {
    if (cart->itemCount < 10) {
        cart->items[cart->itemCount] = item;
        cart->itemCount++;
    } else {
        printf("Cart is full. Cannot add more items.\n");
    }
}
double calculateTotalCost(struct ShoppingCart cart) {
    double total = 0;
    for (int i = 0; i < cart.itemCount; i++) {
        total += cart.items[i].quantity * cart.items[i].price;
    }
    return total;
}
int main() {
    struct Item item1 = {"Shirt", 2, 25.0};
    struct Item item2 = {"Jeans", 1, 50.0};
    struct ShoppingCart cart;
    cart.itemCount = 0;
    addItem(&cart, item1);
    addItem(&cart, item2);
    printf("Total cost: $%.2lf\n", calculateTotalCost(cart));
    return 0;
}
