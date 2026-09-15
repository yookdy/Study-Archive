// fget.c
// fgetc로 파일에서 문자 단위로 읽어 화면에 출력

#include <stdio.h>

int main(void)
{
    FILE *fp = NULL;
    int c;  // 정수 변수에 주의한다.

    fp = fopen("alphabet.txt", "r");
    if (fp == NULL) {
        fprintf(stderr, "원본 파일 alphabet.txt를 열 수 없습니다.\n");
        exit(1);
    }

    while ((c = fgetc(fp)) != EOF)
        putchar(c);

    fclose(fp);
    return 0;
}