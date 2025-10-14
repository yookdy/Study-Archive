// condition.c
// 조건 연산자(삼항 연산자)를 이용한 두 수의 대소 비교

#include <stdio.h>
#define _CRT_SECURE_NO_WARNNING
#define exchange_rate 1400

int main(void){
    int a,b;
    printf("a: ");
    scanf("%d",&a);
    printf("b: ");
    scanf("%d",&b);
    printf("큰수: %d\n",(a>b)?a:b);
    printf("작은 수: %d\n",(a<b)?a:b);
    return 0;
}