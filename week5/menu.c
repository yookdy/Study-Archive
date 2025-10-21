// menu.c
// do-while문을 사용하여 유효한 메뉴 선택 입력 유도

#include <stdio.h>


int main(void){
    int i=0;
    do{
        printf("1. 파일열기");
        printf("2. 파일저장");
        printf("3. 종류");
        printf("4. 하나를 선택");
        scanf("%d",&i);
    } while (i<1||i>3);
    printf("선택된 메뉴:%d",i);
    return 0;
}