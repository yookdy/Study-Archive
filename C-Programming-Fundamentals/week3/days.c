// days.c
// 입력받은 일수를 년, 주, 일 단위로 변환하여 출력

#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

int main(void){
    int da,ye,we;
    printf("총 일수:");
    scanf("%d", &da);
    ye=(da/365);
    we=(da%365)/7;
    da=da-((ye*365)+we*7);

    printf("%d년",ye);
    printf("%d주",we);
    printf("%d일\n",da);
    return 0;
}