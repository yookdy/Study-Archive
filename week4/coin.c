// coin.c
// 난수 생성 함수(rand)를 이용한 동전 던지기 게임

#include <stdio.h>
#define _CRT_SECURE_NO_WARNNING
#include <stdlib.h>

int main(void){
    printf("동전 던지기 게임 시작");
    int c = rand()%2;
    if(c==0)
        printf("앞면");
    else
        printf("뒷면");
    return 0;
}