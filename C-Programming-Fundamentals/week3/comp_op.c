// comp_op.c
// 복합 대입 연산자(+=)를 활용한 변수 값 누적

#include <stdio.h>

int main(void){
    int a=10,b=10;
    printf("x=%d b=%d\n",a,b);
    a+=1;
    printf("(a+=1)이후 a=%d \n",a);
    printf("(b+=1)이후 b=%d \n",a);
}