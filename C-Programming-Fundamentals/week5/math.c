// math.c
// while 무한 루프와 rand 함수를 이용한 산수 퀴즈 프로그램

#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

int main(void){
    int re;
    int i,j,z;
    while(2){
        int i=rand()%20;
        int j=rand()%20;
        int z=rand()%20;
        print("%dx%d+%d=",i,j,z);
        scanf("%d",&re);
        if(i*j+z==re)
            printf("맞았습니다");
        else
            printf("틀렸습니다");
    }
    return 0;
}