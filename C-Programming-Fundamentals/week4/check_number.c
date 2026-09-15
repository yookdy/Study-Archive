// check_number.c
// 논리 연산자를 이용한 입력 값의 0~100 범위 확인

#include <stdio.h>
#define _CRT_SECURE_NO_WARNNING


int main(void){
    int n;
    printf("정수 입력 ");
    scanf("%d",&n);
    if(n>=0&&n<=100){
        printf("입력값은 0과 100사이의 값입니다");
    }
    else{
        printf("입력값은 0과 100사이의 값이 아닙니다");
    }
    return 0;
}