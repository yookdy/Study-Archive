// int_const.c
// 10진수, 16진수, 8진수 형태의 정수 상수 출력 실습

#include <stdio.h>

int main(void){
    printf("%d, %#x,%#o,\n",128,128,128);
    //%d는 인자를 10진수 
    //%#x는 인자를 **16진수(hexadecimal)
    //%#o는 인자를 **8진수
    return 0;
}