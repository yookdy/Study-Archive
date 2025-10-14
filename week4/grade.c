// grade.c
// 점수 구간에 따른 학점(A~F) 등급 부여

#include <stdio.h>

int main(void){
    int s;
    char g;
    printf("성적: ");
    scanf("%d", &s);
    if (s>=90)
        g='A';
    else if(s>=80)
        g='B';
    else if(s>=70)
        g='C';
    else if(s>=60)
        g='D';
    else if(s>=50)
        g='E';
    else
        g='F';
    printf("학점:%c",g);
    return 0;
}