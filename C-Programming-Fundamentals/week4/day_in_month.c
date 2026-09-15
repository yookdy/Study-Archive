// day_in_month.c
// switch-case문을 이용한 월별 일수 계산 및 출력

// 
// #include <stdio.h>
// #define _CRT_SECURE_NO_WARNNING


// int main(void){
//     int m, d;
//     printf("일수를 알고 싶은 달:");
//     scanf("%d", &m);
//     switch(m){
//     case 2:
//         d=28;
//         break;
//     case 4:
//     case 6:
//     case 9:
//     case 11:
//         d=30;
//         break;
//     default:
//         d=31;
//         break;
//     }
//     printf("%d월의 일수: %d",m,d);
//     return 0;
// }


#include <stdio.h>
#define _CRT_SECURE_NO_WARNNING


int main(void){
    int m,d;
    printf("일수를 알고 싶은 달: ");
    scanf("%d",&m);
    switch (m){
        case 2:
            d=28;
            break;
        case 4:
        case 6:
        case 9:
        case 11:
            d=28;
            break;
        default:
            d=31;
            break;
    }
    printf("%d월의 일수는 %d",m,d);
    return 0;
}