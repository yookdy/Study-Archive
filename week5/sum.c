// sum.c
// while문을 이용한 1부터 1000까지의 정수 합계 계산

#include <stdio.h>

int main(void){
    int i,sum;
    i=1;
    sum=0;
    while (i<=1000){
        sum+=i;
        i++;
    }
    printf("합:%d",sum);
    return 0;
}