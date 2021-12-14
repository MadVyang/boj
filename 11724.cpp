#include <stdio.h>

int N, M;
bool ver[1005];
bool edge[1005][1005];

void sol(int n)
{
    if (ver[n])
        return;
    ver[n] = true;
    // printf("      %d\n", n);
    for (int i = 1; i <= N; i++)
    {
        if (!edge[n][i])
            continue;
        sol(i);
    }
}

int main()
{
    int x, y;
    scanf("%d%d", &N, &M);
    for (int i = 0; i < M; i++)
    {
        scanf("%d%d", &x, &y);
        edge[x][y] = true;
        edge[y][x] = true;
    }

    int count = 0;
    for (int i = 1; i <= N; i++)
    {
        if (ver[i])
            continue;
        // printf("   %d\n", i);
        count++;
        sol(i);
    }

    printf("%d\n", count);
    return 0;
}