// score1.c
// 배열 선언 및 반복문을 이용한 배열 요소 접근 및 출력

#include <stdio.h>
#define SIZE 5

int main(void){
    int i;
    int scores[SIZE];
    int scores[0];
    int scores[1];
    int scores[2];
    int scores[3];
    int scores[4];
    for (i=0; i<SIZE; i++){
        printf("scores[%d]=%d\n",i,scores[i]);
    }
    return 0;
}