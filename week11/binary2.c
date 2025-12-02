// binary2.c
// fread를 사용해 바이너리 파일에서 정수 배열 읽기

#include <stdio.h>
#define SIZE 10

int main(void)
{
    int buffer[SIZE];
    FILE *fp = NULL;
    int i;

    fp = fopen("binary.bin", "rb");

    if (fp == NULL) {
        fprintf(stderr, "binary.bin 파일을 열 수 없습니다.");
        return 1;
    }

    fread(buffer, sizeof(int), SIZE, fp);

    for (i = 0; i < SIZE; i++)
        printf("%d ", buffer[i]);

    fclose(fp);
    return 0;
}