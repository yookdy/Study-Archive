// over_under.c
// 부동소수점 자료형의 오버플로우 및 언더플로우 발생 확인

#include <stdio.h>

int main(void){
    float x=1e39;
    float y=1.23456e-46;

    printf("x=%e\n",x);
    printf("y=%e\n",y);
    return 0;
}