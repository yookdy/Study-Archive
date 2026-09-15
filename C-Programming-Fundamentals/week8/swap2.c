// swap2.c
// 포인터 인자를 이용한 두 변수 값의 교환(Swap) 구현

#include <stdio.h>

void swap(int *px, int *py);

int main(void) {
    int n = 300, m = 400;

    printf("swap() 호출 전: n=%d, m=%d\n", n, m); 
    swap(&n, &m); 
    printf("swap() 호출 후: n=%d, m=%d\n", n, m);

    return 0;
}

void swap(int *px, int *py) {
    int t;

    t = *px;
    *px = *py;
    *py = t;  
}