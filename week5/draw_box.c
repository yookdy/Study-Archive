// draw_box.c
// 반복문을 이용하여 테두리만 있는 사각형 박스 그리기

#include <stdio.h>

int main(void){
    int i;
    printf("**********\n");
    for(i=0;i<5;i++){
        printf("*        *\n");
    }
    printf("**********");
    return 0;
}