#include <stdio.h>
#include <string.h>
#include <stdbool.h>
int countWords(char str[]) {
    int count = 0;
    bool inWord = false;
    for (int i = 0; i < strlen(str); i++) {
        if (str[i] == ' ' || str[i] == '\n' || str[i] == '\t') {
            inWord = false;
        } else if (!inWord) {
            inWord = true;
            count++;
        }
    }
    return count;
}

int main() {
    char str[] = "Hello world, this is a simple test.";
    printf("Number of words: %d\n", countWords(str));
    return 0;
}
