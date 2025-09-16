// get_ascii.c
// 문자의 아스키(ASCII) 코드 값 확인 및 입출력 실습

#include <stdio.h>

int main(void){
    char c;
    c='A';
    printf("A의 아스키 코드=%d\n",c);
    printf("문자를 입력하시오");
    c=getchar();
    printf("%c의 아스키 코드=%d",c,c);
    return 0;
}