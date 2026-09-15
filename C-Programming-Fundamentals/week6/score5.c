// score5.c
// 배열 선언과 동시에 초기화(Initialization) 및 요소 출력

#include <stdio.h>
#define SIZE 5

int main(void){
    int i;
    int scores[SIZE]={23,43,41,67,21};
    for(i=0; i<SIZE; i++)
        printf("scores[%d]=%d\n",i,scores[i]);
    return 0;
}