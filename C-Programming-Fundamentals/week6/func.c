// func.c
// 사용자 정의 함수(get_integer)를 통한 값 입력 및 덧셈 연산

#include <stdio.h>

int get_integer(){
    int value;
    printf("정수 입력:");
    scanf("%d", &value);
    return value;
}

int main(void){
    int x, y;
    x=get_integer();
    y=get_integer();
    int re=x+y;
    printf("두수의 합: %d", re);
    return 0;
}