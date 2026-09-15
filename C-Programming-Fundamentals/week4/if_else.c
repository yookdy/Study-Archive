// if_else.c
// 입력받은 온도의 영하 및 영상 판별

#include <stdio.h>
#define _CRT_SECURE_NO_WARNING

int main(void){
    int tem;
    printf("온도: ");
    scanf("%d", &tem);
    if(tem>=0){
        printf("영상");
    }
    else{
        printf("영하");
    }
    printf("현재는 온도: %d",tem);
    return 0;
}