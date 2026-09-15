// floating.c
// float형과 double형 변수의 유효 숫자 정밀도 차이 비교

#include <stdio.h>

int main(void){
    float fvalue=1234567890.12345678901234567890;
    double dvalue=1234567890.12345678901234567890;
    printf("float형 변수=35.25f\n",fvalue);
    printf("double형 변수=35.25f\n",dvalue);
    return 0;
}