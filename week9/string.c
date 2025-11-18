// string.c
// 다양한 방식의 문자열 배열 선언 및 초기화 방법

#include <stdio.h>


int main(void){
    char str1[6]="Seoul";
    char str2[3]={'i', 's', '\0'};
    char str3[]="the capital city of Korea.";
    printf("%s %s %s\n", str1,str2, str3);
    return 0;
}