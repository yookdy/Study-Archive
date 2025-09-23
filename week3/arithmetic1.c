// arithmetic1.c
// 정수의 사칙연산 및 나머지 연산(%) 수행

#include <stdio.h>
#define _CRT_SECURE_NO_WARNNING

int main(void){
    int a,b, re;
    printf("두 정수 입력:");
    scanf("%d %d", &a, &b);
    re=a+b;
    printf("%d %% %d = %d\n", a, b, re);
    re=a-b;
    printf("%d %% %d = %d\n", a, b, re);
    re=a*b;
    printf("%d %% %d = %d\n", a, b, re);
    re=a/b;
    printf("%d %% %d = %d\n", a, b, re);
    re=a%b;
    printf("%d %% %d = %d\n", a, b, re);
    return 0;
}