#include <stdio.h>

void soma(int* num, int a, int b){ //ponteiro É um endereço
    *num = a + b;
    printf("%d\n", *num);
}


int main(){
    int num;
    int a, b;
    a = 10;
    b = 15;
    soma(&num, a, b); // passa endereço da variavel num
    return 0;
}