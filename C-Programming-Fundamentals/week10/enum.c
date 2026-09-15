// enum.c
// (파일명과 달리) 공용체의 메모리 공유 확인

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