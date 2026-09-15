// gugu1.c
// while문을 사용하여 구구단 중 특정 단 출력

#include <stdio.h>

int main(void){
    int n=1;
    int i=1;
    printf("출력하고 싶은단: ");
    while (i<=9){
        printf("%d*%d=%d\n",n,i,n*i);
        i++;
    }
    return 0;
}