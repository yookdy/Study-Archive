// bit_op.c
// 비트 논리 연산자(AND, OR, XOR, NOT) 결과 16진수 출력

#include <stdio.h>

int main(void){
    int a=9,b=10;
    printf("%08X & %08X = %08X\n",a,b,a&b);
    printf("%08X & %08X = %08X\n",a,b,a|b);
    printf("%08X & %08X = %08X\n",a,b,a^b);
    printf("~%08X = %08X\n",a,~a);

}