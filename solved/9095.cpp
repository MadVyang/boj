#include <stdio.h>

int N;
bool mem[20][20][20];

int pact(int n)
{
    if (n == 0)
        return 1;
    return pact(n - 1) * n;
}

int cal(int x, int y, int z)
{
    return pact(x + y + z) / (pact(x) * pact(y) * pact(z));
}

int sol(int x, int y, int z)
{
    if (x < 0)
        return 0;
    if (mem[x][y][z])
        return 0;
    mem[x][y][z] = true;

    int r = cal(x, y, z);
    // printf("   %d    %d %d %d\n", r, x, y, z);
    if (x >= 2)
        r += sol(x - 2, y + 1, z);
    if (x >= 3)
        r += sol(x - 3, y, z + 1);
    return r;
}

int main()
{
    int k;
    scanf("%d", &N);
    for (int i = 0; i < N; i++)
    {
        scanf("%d", &k);
        printf("%d\n", sol(k, 0, 0));
    }
    return 0;
}