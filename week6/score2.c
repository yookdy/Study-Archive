// score2.c
// 배열을 활용한 5개 성적 입력, 합계 및 평균 계산 수행

#include <stdio.h>
#define STUDENTS 5

int main(void){
    int i, average;
    int sum =0;
    int scores[STUDENTS];
    for(i=0; i<STUDENTS; i++){
        printf("학생의 성적: ");
        scanf("%d",&scores[i]);
    }
    for(i=0; i<STUDENTS; i++)
        sum+=scores[i];
    average=sum/STUDENTS;
    printf("평균:%d\n",average);
    return 0;
}