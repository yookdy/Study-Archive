// p_array1.c
// 배열의 이름과 첫 번째 요소의 메모리 주소 비교 확인

#include <stdio.h>


int main(void){
    int a[]={10,20,30,40,50};
    printf("배열의 이름=%u\n", a);
    printf("첫번째 원소의 주소=%u", &a[0]);
    
    return 0;
}