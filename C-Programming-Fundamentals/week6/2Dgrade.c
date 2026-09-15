// 2Dgrade.c
// 2차원 배열을 이용한 과목 및 평가 항목별 성적표 출력

#include <stdio.h>
#define SIZE 3

int main(void){
    int i,j;
    char name[SIZE][10]={"c언어 ","파이썬","수학  "};
    char standard[6][10]={"       ", "출석","태도" ,"과제", "중간","기말"};
    int s[3][5]={{10, 10, 10,35, 25},{10, 10, 10, 35, 30},{10, 10, 10, 25, 30}};
    for(i=0; i<6; i++){
        printf("%s ",standard[i]);
    }
    printf("\n");
    for(i=0; i<3; i++){
        printf("%s  ",name[i]);
        for(j=0; j<5; j++){
            printf(" %d  ", s[i][j]);
        }
        printf("\n");
    }
    
    return 0;
}