// overflow.c
// short형 변수의 최대값 초과로 인한 정수 오버플로우 현상 확인

#include <stdio.h>

int main(void){
    short s=32767;
    s=s+1;
    printf("s=%d",s);
    return 0;
}