// factorial.c
// for문을 이용한 정수의 팩토리얼(계승) 계산

#include <stdio.h>

int main(void){
    int fact=1;
    int i,n;
    printf("정수: ");
    scanf("%d",&n);
    for(i=1;i<=n; i++){
        fact=fact*i;
    }
    printf("%d!은 %d입니다\n",n,fact);
    return 0;
}