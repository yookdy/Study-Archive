// string2.c
// 배열 인덱스를 이용한 문자열 내 특정 문자 수정

#include <stdio.h>


int main(void){
    char str[]="komputer";

    printf("%s\n", str);
    str[0]='c';
    printf("%s\n", str);
    return 0;
}