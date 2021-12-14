#include <stdio.h>

int N;
int arr[1003][3];
int mem[1003][3];

int min(int a, int b)
{
    return a > b ? b : a;
}

int sol(int i, int v)
{
    if (i == -1)
        return 0;
    if (v != -1 && mem[i][v])
        return mem[i][v];

    int r0 = 99999999, r1 = 99999999, r2 = 99999999;
    if (v != 0)
        r0 = sol(i - 1, 0) + arr[i][0];
    if (v != 1)
        r1 = sol(i - 1, 1) + arr[i][1];
    if (v != 2)
        r2 = sol(i - 1, 2) + arr[i][2];
    int r = min(min(r0, r1), r2);
    mem[i][v] = r;
    return r;
}

int main()
{
    scanf("%d", &N);
    for (int i = 0; i < N; i++)
    {
        scanf("%d%d%d", &arr[i][0], &arr[i][1], &arr[i][2]);
    }
    printf("%d\n", sol(N - 1, -1));

    return 0;
}