// nested_loop2.c
// 중첩 반복문을 활용하여 별(*)로 사각형 패턴 출력

#include <stdio.h>

int main(void){
    int x,y;
    for(y=0; y<5;y++){
        for(x=0;x<10;x++){
            printf("*");
        }
        printf("\n");
    }    
    return 0;
}