// atoi.c
// atoi와 sscanf 등을 활용한 문자열과 정수 변환

#include <stdio.h>
#include <stdlib.h>


int main(void){
    const char s[]= "100";
    char t[100]="";
    int i;

    printf("%d \n", atoi("100"));
    sscanf(s, "%d", &i);
    sprint(t, "%d", 100);
    return 0;
}