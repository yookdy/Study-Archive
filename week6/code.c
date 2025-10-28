// C589026_code.c
// 문자형 배열과 반복문을 이용한 알파벳 소문자 생성 및 출력

#include <stdio.h>
#define SIZE 26

int main(void){
    int i;
    char codes[SIZE];
    for (i=0; i<SIZE; i++){
       codes[i]='a'+i;
    }
    for(i=0; i<SIZE; i++){
        printf("%c ",codes[i]);
    }
    printf("\n");
    return 0;
}