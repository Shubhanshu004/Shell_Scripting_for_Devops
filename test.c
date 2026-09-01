#include <stdio.h>

void greet() {
    int local_var = 42;   // stack pe
    printf("Value: %d\n", local_var);
}

int main() {
    greet();
    return 0;
}
