// gugu_tot.c
// 중첩 for문을 이용한 구구단 전체(1~9단) 출력

#include <stdio.h>

int main(void){
    int i,k;
    for(i=1;i<=9;i++){
        for(k=1;k<=9; k++){
            printf("%d x%d=%d\n",i,k,i*k);
        }
    }
    return 0;
}