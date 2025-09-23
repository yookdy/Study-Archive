// comp2_op.c
// 복합 대입 연산자(+=, *=)를 활용한 변수 값 변경 및 연산

#include <stdio.h>

int main(void){
    int a=11,b=17;
    printf("x=%d b=%d\n",a,b);
    a+=1;
    printf("(a+=1)이후 a=%d \n",a);
    b*=2;
    printf("(b*=2)이후 b=%d \n",b);
}