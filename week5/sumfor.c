// sumfor.c
// for문과 if문을 조합하여 구구단 4단만 선별 출력

#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

int main(void){
    int i,j;
    i=1;
    j=1;
    for(i=1; i<10; i++){
        for(j=1; j<10; j++){
            if(i==4){
                printf("%dx%d=%d\n",i,j,i*j);
            }
        }
    }
    return 0;
}