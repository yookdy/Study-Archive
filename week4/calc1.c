// calc1.c
// if-else if문을 사용한 문자기반 사칙연산 계산기

#include <stdio.h>

int main(void){
    char g;
    int a,b;
    printf("수식을 입력하세요: ");
    scanf("%d %c %d",&a,&g,&b);
    if(g=='+')
        printf("%d\n", a+b);
    else if(g=='-')
        printf("%d\n", a-b);
    else if(g=='*')
        printf("%d\n", a*b);
    else if(g=='/')
        printf("%d\n", a/b);
    else
        printf("지원되지 않는 연산자\n");
    return 0;
}