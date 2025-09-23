// prep.c
// 연산자 우선순위와 결합 법칙에 따른 수식 계산 순서 확인

#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

int main(void){
    int x,y,z,e,re;
    x=1;
    y=2;
    z=3;
    e=4;
    re=x+y*z/e;
    printf("값: %d\n",re);
    re=(x*y)*z/e;
    printf("값: %d\n",re);
    re=x=y=re;
    printf("값: %d\n",re);
    return 0;
}