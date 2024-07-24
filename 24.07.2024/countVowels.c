#include <stdio.h>
#include <string.h>
int countVowels(char str[]) {
    int count = 0;
    for (int i = 0; i < strlen(str); i++) {
        char ch = tolower(str[i]);
        if (ch == 'a' || ch == 'e' || ch == 'i' || ch == 'o' || ch == 'u')
            count++;
    }
    return count;
}

int main() {
    char str[] = "Hello World";
    printf("Number of vowels: %d\n", countVowels(str));
    return 0;
}
