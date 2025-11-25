// student.c
// 구조체 정의, 문자열 복사 및 학생 정보 출력

#include <stdio.h>
#include <stdlib.h>
#include <string.h> 

struct student{
    double grade;
    int age;
    char school[100];
    char name[20];
    char schoolnumber[20];
};

int main(void){
    struct student s;
    
    
    s.grade = 4.13;
    strcpy(s.name, "육도연");
    s.age = 22;
    strcpy(s.school, "홍익대학교");
    strcpy(s.schoolnumber, "c589036");

   
    printf("이름: %s\n", s.name);
    printf("나이: %d\n", s.age);
    printf("학교: %s\n", s.school);
    printf("학번: %s\n", s.schoolnumber);
    printf("성적: %.2lf\n", s.grade); 
    
    return 0;
}