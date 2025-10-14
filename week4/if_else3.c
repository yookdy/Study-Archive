// if_else3.c
// 점수에 따른 합격 및 불합격 여부와 메시지 출력

#include <stdio.h>

int main(void){
    int s;
    printf("성적: ");
    scanf("%d", &s);
    if(s>=60){
        printf("합격");
        printf("장학금 가능");
    }
    else{
        printf("불합격");
        printf("다시 도전");
    }
    return 0;
}