#include <stdio.h>
#define MAX 1000
int stack[MAX];
int top = -1;
void push(int x) {
    if (top >= MAX - 1) {
        printf("Stack Overflow\n");
        return;
    }
    stack[++top] = x;
}
int pop() {
    if (top < 0) {
        printf("Stack Underflow\n");
        return -1;
    }
    return stack[top--];
}
int peek() {
    if (top < 0) {
        printf("Stack is Empty\n");
        return -1;
    }
    return stack[top];
}
int isEmpty() {
    return top < 0;
}
int main() {
    push(10);
    push(20);
    push(30);
    printf("%d popped from stack\n", pop());
    printf("Top element is %d\n", peek());
    return 0;
}
