// power.c
// 사용자 정의 함수를 이용한 거듭제곱(x의 y승) 계산

#include <stdio.h>

int get_integer(){
    int value;
    printf("정수 입력:");
    scanf("%d", &value);
    return value;
}
int power(int x, int y){
    int i, re =1;
    for(i=0; i<y; i++){
        re*=x;
    }
    return re;
}

int main(void){
    int x, y;
    x=get_integer();
    y=get_integer();
    int re=power(x,y);
    printf("%d의 %d승: %d", x, y ,re);
    return 0;
}