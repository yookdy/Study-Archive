// add1.c
// 고정된 변수 값을 이용한 덧셈 연산

#include <stdio.h>

int main(void){
   int x;
   int y;
   int sum;
   x=100;
   y=200;
   sum=x+y;
   printf("두 수의 합: %d",sum);
   return 0;
}