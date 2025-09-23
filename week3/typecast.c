// typecast.c
// 형변환 연산자((type))를 이용한 명시적 형변환 및 연산 결과 확인

#include<stdio.h>

int main(void){
    int a;
    double b;
    b=5/3;
    printf("(5/3)=%lf\n",b);
    b=(double)5/3;
    printf("(double)5/3=%lf\n",b);
    a=4.23+42.3;
    printf("4.23+42.3%d\n",a);
    a=(int)4.23+(int)42.3;
    printf("(int)4.23+(int)42.3=%d\n",a);
    return 0;

}