// get_max.c
// 함수를 활용하여 입력받은 두 정수 중 큰 값 반환

#include <stdio.h>

int get_integer(){
    int value;
    printf("정수 입력:");
    scanf("%d", &value);
    return value;
}

int get_max(int x, int y){
    if(x>y)return(x);
    else return(y);
}

int main(void){
    int a, b;
    a= get_integer();
    b= get_integer();
    printf("두수 중에서 큰수는 %d입니다", get_max(a,b));
    return 0;
}