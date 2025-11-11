// address_of.c
// 주소 연산자(&)를 사용하여 각 변수의 메모리 주소 출력

#include <stdio.h>

int main(void){
    int poi=20;
    char poc='A';
    double pod=30.5;

    printf("poi의 주소: %p\n",&poi);
    printf("poc의 주소: %p\n",&poc);
    printf("pod의 주소: %p\n",&pod);
}