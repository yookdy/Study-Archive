// bit_shift.c
// 비트 이동 연산자(<<, >>)를 이용한 시프트 연산 수행

#include <stdio.h>

int main(void){
    int a=34;
    printf("%d <<3=%d\n",a,a<<2);
    printf("%d >>3=%d\n",a,a>>2);
    return 0;
}