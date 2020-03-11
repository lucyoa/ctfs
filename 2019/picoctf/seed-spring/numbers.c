#include <stdio.h>

int main(int argc, char *argv[]) {
    srand(time(0) + atoi(argv[1]));
    for(int i = 0; i<30; i++)
        printf("%d\n", rand() & 0xf);

    return 0;
}
