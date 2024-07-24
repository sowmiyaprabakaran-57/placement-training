#include <stdio.h>
int main() {
    FILE *file;
    char data[100];
    file = fopen("example.txt", "w");
    if (file == NULL) {
        printf("Unable to open file for writing.\n");
        return 1;
    }
    printf("Enter some text to write to the file: ");
    fgets(data, sizeof(data), stdin);
    fprintf(file, "%s", data);
    fclose(file);
    file = fopen("example.txt", "r");
    if (file == NULL) {
        printf("Unable to open file for reading.\n");
        return 1;
    }
    printf("Contents of the file:\n");
    while (fgets(data, sizeof(data), file)) {
        printf("%s", data);
    }
    fclose(file);
    return 0;
}
