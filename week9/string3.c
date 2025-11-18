// string3.c
// 반복문을 통해 NULL 문자를 찾으며 문자열 길이 계산

#include <stdio.h>


int main(void){
    char str[]="A barking dog never bites";
    int i=0;
    while (str[i]!=0)
        i++;
    printf("문자열 %s의 길이는 %d입니다\n", str,i);
    return 0;
}