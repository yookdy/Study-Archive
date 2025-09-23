// incdec.c
// 전위 증가 연산자(++)를 통한 변수 값 변화 확인

#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

int main(void){
    int a,b;
    a=1;
    b=++a;
    printf("a=%d b=%d \n",a,b);
    b=++a;
    printf("a=%d b=%d", a,b);
    return 0;
}