// leap_year.c
// 논리 연산자를 활용한 윤년 여부 판별

#include <stdio.h>
#define _CRT_SECURE_NO_WARNNING

int main(void){
    int y;
    printf("연도: ");
    scanf("%d", &y);
    if(y%4==0&&y%100!=0  || y%400==0)
        printf("%d년은 윤년",y);
    else
        printf("%d년은 윤년X",y);
    return 0;
}