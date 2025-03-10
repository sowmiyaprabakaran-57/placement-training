#include <stdio.h>
int findSecondLargest(int arr[], int n) {
    int first = arr[0], second = -1;
    for (int i = 1; i < n; i++) {
        if (arr[i] > first) {
            second = first;
            first = arr[i];
        } else if (arr[i] > second && arr[i] != first) {
            second = arr[i];
        }
    }
    return second;
}

int main() {
    int arr[] = {12, 35, 1, 10, 34, 1};
    int n = sizeof(arr) / sizeof(arr[0]);
    int result = findSecondLargest(arr, n);
    if (result != -1)
        printf("Second largest element is %d\n", result);
    else
        printf("There is no second largest element\n");
    return 0;
}
