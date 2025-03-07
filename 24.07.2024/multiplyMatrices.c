#include <stdio.h>
void multiplyMatrices(int firstMatrix[][3], int secondMatrix[][3], int result[][3], int rowFirst, int columnFirst, int rowSecond, int columnSecond) {
    for(int i = 0; i < rowFirst; ++i) {
        for(int j = 0; j < columnSecond; ++j) {
            result[i][j] = 0;
        }
    }
    for(int i = 0; i < rowFirst; ++i) {
        for(int j = 0; j < columnSecond; ++j) {
            for(int k = 0; k < columnFirst; ++k) {
                result[i][j] += firstMatrix[i][k] * secondMatrix[k][j];
            }
        }
    }
}
int main() {
    int firstMatrix[3][3] = {{1, 2, 3}, {4, 5, 6}, {7, 8, 9}};
    int secondMatrix[3][3] = {{9, 8, 7}, {6, 5, 4}, {3, 2, 1}};
    int result[3][3];
    multiplyMatrices(firstMatrix, secondMatrix, result, 3, 3, 3, 3);
    printf("Resultant matrix: \n");
    for(int i = 0; i < 3; i++) {
        for(int j = 0; j < 3; j++) {
            printf("%d ", result[i][j]);
        }
        printf("\n");
    }
    return 0;
}
