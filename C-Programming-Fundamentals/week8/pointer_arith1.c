// pointer_arith1.c
// 포인터 자료형 크기에 따른 주소 증감 연산 결과 확인

#include <stdio.h>


int main(void){
    char *pc;
    int *pi;
    double *pd;
    pc =(char *)10000;
    pi =(int *)10000;
    pd =(double *)10000;
    printf("증가 전 pc=%d pi=%d pd=%d",pc,pi,pd);
     pc++;
     pi++;
     pd++;
     printf("증가후 pc=%d pi=%d pd=%d",pc,pi,pd);
    return 0;
}