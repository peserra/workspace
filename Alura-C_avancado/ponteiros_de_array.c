#include <stdio.h>
#include<stdlib.h>

int soma(int *array_inteiros, int tamanho){ //posso receber um array numa função desse jeito
   int soma = 0;
   for(int i = 0; i < tamanho; i++){
    soma += *(array_inteiros + i);
   }
    return soma;
}

int main(){
    int nums[3];
    nums[0] = 10;
    nums[1] = 20;
    nums[2] = 30;
    int total = soma(nums, 3);
    printf("Soma: %d\n", total);
    return 0;
}