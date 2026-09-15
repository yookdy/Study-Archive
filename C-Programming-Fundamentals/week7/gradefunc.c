// gradefunc.c
// 점수 입력에 따른 학점(A~F) 출력 및 입력 횟수 카운트

#include <stdio.h>

int count=0;

int grade(int score){
    if(score<0&&score>100){
        printf("입력이 잘 못 되었습니다");
    }
    if (score>=90){
        count++;
        printf("A\n");
    }
    else if(score>=80){
        count++;
        printf("B\n");
    }
    else if(score>=70){
        count++;
        printf("C\n");
    }
    else if(score>=60){
        count++;
        printf("D\n");
    }
    else if(score>=50){
        count++;
        printf("E\n");
    }
    else{
        count++;
        printf("F\n");
    }
}


int main(void){
    int score;
    char name[30];
    int check=0;
    while(check<1){
        printf("과목과 성적을 입력하세요: ");
        scanf("%c, %d", name, &score);
        grade(score);
        if(check>=4){
            printf("입력횟수가 초과 되었습니다");
        }
        continue;
    }
    return 0;
}