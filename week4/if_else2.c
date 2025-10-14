// if_else2.c
// if-else문을 이용한 정수의 홀수 및 짝수 판별

#include <stdio.h>

int main(void){
    int num;
    printf("정수: ");
    scanf("%d", &num);
    if(num%2==0){
        printf("짝수");
    }
    else{
        printf("홀수");
    }
    return 0;
}