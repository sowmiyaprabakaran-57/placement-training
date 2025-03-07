#include <stdio.h>
#include <string.h>
struct Product {
    char name[50];
    int quantity;
    double price;
};
void updateQuantity(struct Product *product, int soldQuantity) {
    if (product->quantity >= soldQuantity) {
        product->quantity -= soldQuantity;
        printf("Updated quantity for %s: %d\n", product->name, product->quantity);
    } else {
        printf("Insufficient stock for %s\n", product->name);
    }
}
int main() {
    struct Product product1 = {"Widget", 100, 10.0};
    struct Product product2 = {"Gadget", 50, 20.0};
    updateQuantity(&product1, 20);
    updateQuantity(&product2, 60);
    printf("%s (Qty: %d, Price: $%.2lf)\n", product1.name, product1.quantity, product1.price);
    printf("%s (Qty: %d, Price: $%.2lf)\n", product2.name, product2.quantity, product2.price);
    return 0;
}
