// pointer1.c
// 포인터 변수 선언, 주소 저장 및 역참조 연산자 활용

#include <stdio.h>


int main(void){
    int number=10;
    int *p;
    p=&number;
    printf("number의 주소=%p", &number);
    printf("포인터의 값=%p",p);
    printf("number의 값=%d",number);
    printf("포인터의 값%d",*p);
    return 0;
}