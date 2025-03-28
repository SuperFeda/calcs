#include <stdio.h>


int main() {
    float a, b, result;
    char operation;

    printf("Enter first num >>");
    scanf("%f", &a);

    printf("Enter second num >>");
    scanf("%f", &b);

    printf("Enter operation (+, -, *, /) >>");
    scanf("%s", &operation);

    if (operation == '+') {
        result = a + b;
    } else if (operation == '-') {
        result = a - b;
    } else if (operation == '*') {
        result = a * b;
    } else if (operation == '/') {
        if (b != 0) {
            result = a / b;
        } else {
            result = 0;
            printf("you cannot divide by zero!\n");
        }
    }

    printf("%f", result);

    return 0;
}
