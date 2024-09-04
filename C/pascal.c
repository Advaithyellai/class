#include <stdio.h>

int main() {
    printf("How many rows of Pascal's triangle do you want: ");
    int N;
    scanf("%d", &N);
    int a[N];
    a[0] = 0;
    a[1] = 1;
    a[2] = 0;
    printf("1\n");
    for (int i = 0; i<N-1; i++) {
        int b[i+2];
        for (int j = 0; j<i+2; j++) {
            b[j] = a[j+1]+a[j];
        }
        a[0] = 0;
        for (int k = 0; k<i+2; k++) {
            a[k+1] = b[k];
            printf("%d ", b[k]);
        }
        a[i+3] = 0;
        printf("\n");
    }
}