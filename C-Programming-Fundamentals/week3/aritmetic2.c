// aritmetic2.c
// double형 변수를 이용한 실수의 사칙연산 입출력

//arithmetic2.c
#include <stdio.h>
#define _CRT_SECURE_NO_WARNNING

int main(void){
    double a,b, re;
    printf("두 실수 입력:");
    scanf("%lf %lf", &a, &b);
    re=a+b;
    printf("%lf+%lf=%lf\n",a,b,re);
    re=a-b;
    printf("%lf-%lf=%lf\n",a,b,re);
    re=a*b;
    printf("%lfx%lf=%lf\n",a,b,re);
    re=a/b;
    printf("%lf/%lf=%lf\n",a,b,re);
    return 0;
}