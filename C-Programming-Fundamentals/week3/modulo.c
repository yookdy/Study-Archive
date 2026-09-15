// modulo.c
// 나머지 연산자를 활용하여 초 단위 시간을 분과 초로 변환

#include <stdio.h>
#define _CRT_SECURE_NO_WARNNING
#define se_minute 60

int main(void){
    int inp,min,sec;
    printf("초 단위 시간 입력");
    scanf("$%d", &inp);
    min=inp/se_minute;
    sec=inp%se_minute;
    printf("%d초: %d분 %d초", inp, min, sec);

    return 0;
}