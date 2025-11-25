// union.c
// 공용체(Union) 선언과 데이터 저장 방식 이해

#include <stdio.h>

union example {
    int i;
    char c;
};

int main(void)
{
    union example data;

    data.c = 'A';
    printf("data.c:%c data.i:%i\n", data.c, data.i);

    data.i = 10000;
    printf("data.c:%c data.i:%i\n", data.c, data.i);
}