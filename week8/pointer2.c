// pointer2.c
// 포인터의 역참조(*)를 이용하여 변수 값을 간접 변경

#include <stdio.h>


int main(void){
    int number =10;
    int *p;
    p=&number;
    printf("number의 값 =%d",number);
    *p=20;
    printf("number의 값 =%d", number);
    return 0;
}