// sumwhile.c
// while과 if문을 사용하여 특정 범위 내 4의 배수 출력

//4의 배수 110~930까지

#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

int main(void){
    int i, sum;
    i=0;
    sum=0;
    while(i<1000){
        i++;
        if(i>101 && i<930){
            if(i%4==0)
                printf("%d  ", i);
        }
    }
    return 0;
}