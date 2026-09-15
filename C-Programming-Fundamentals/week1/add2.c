// add2.c
// scanf로 입력받은 두 수의 합 계산

#include <stdio.h>

int main(void){
   int x;
   int y;
   int sum;
   printf("첫번째 수: ");
   scanf("%d",&x);
   printf("두번째 수:");
   scanf("%d",&y);
   sum=x+y;
   printf("합: %d", sum);
   return 0;
}