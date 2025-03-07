#include <stdio.h>
#define MAX 1000
int queue[MAX];
int front = -1, rear = -1;
void enqueue(int x) {
    if (rear >= MAX - 1) {
        printf("Queue Overflow\n");
        return;
    }
    if (front == -1) front = 0;
    queue[++rear] = x;
}
int dequeue() {
    if (front == -1 || front > rear) {
        printf("Queue Underflow\n");
        return -1;
    }
    return queue[front++];
}
int isEmpty() {
    return front == -1 || front > rear;
}
int main() {
    enqueue(10);
    enqueue(20);
    enqueue(30);
    printf("%d dequeued from queue\n", dequeue());
    printf("Front element is %d\n", queue[front]);
    return 0;
}
