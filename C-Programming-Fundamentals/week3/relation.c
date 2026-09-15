// relation.c
// 관계 연산자(==, !=, >)를 이용한 두 정수의 대소 및 동등 비교

#include <stdio.h>
#define _CRT_SECURE_NO_WARNNING

int main(void){
    int a, b;
    printf("두개의 정수: ");
    scanf("%d %d",&a, &b);
    printf("%d==%d: %d\n",a,b,a==b);
    printf("%d!=%d: %d\n,",a,b,a!=b);
    printf("%d>%d: %d\n",a,b,a>b);
    printf("%d<%d: %d\n",a,b,a<b);
    printf("%d<=%d: %d\n",a,b,a>=b);
    printf("%d>=%d: %d\n",a,b,a<=b);
    return 0;
}