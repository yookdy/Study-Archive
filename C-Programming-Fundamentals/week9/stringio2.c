// stringio2.c
// gets_s 함수를 사용하여 문자열 입력받기 및 출력

#include <stdio.h>


int main(void){
    char name[100];
    char address[100];

    printf("이름이 어떻게 되시나요?");
    gets_s(name, 99);
    printf("어디에 사시나요?");
    gets_s(address, 99);
    printd("안녕하세요, %s에 사는 %s씨\n.", address, name);
    return 0;
}