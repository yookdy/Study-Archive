// binary1.c
// fwrite를 사용해 정수 배열을 바이너리 파일로 저장

#include <stdio.h>
#define SIZE 10

int main(void)
{
    int buffer[SIZE] = { 10, 20, 30, 40, 50, 60, 70, 80, 90, 100 };
    FILE *fp = NULL;

    fp = fopen("binary.bin", "wb");
    if (fp == NULL) {
        fprintf(stderr, "binary.bin 파일을 열 수 없습니다.");
        return 1;
    }

    fwrite(buffer, sizeof(int), SIZE, fp);
    fclose(fp);
    return 0;
}