#include <iostream>
#include <stdio.h>

using namespace std;

int N, M;
int arr[1003][1003];
int mem[1003][1003];
bool visited[1003][1003];

int max(int a, int b)
{
    return a > b ? a : b;
}

int sol(int y, int x)
{

    if (y < 0)
        return 0;
    if (x < 0)
        return 0;

    if (visited[y][x])
        return mem[y][x];
    visited[y][x] = true;

    mem[y][x] = max(sol(y - 1, x), sol(y, x - 1)) + arr[y][x];
    return mem[y][x];
}

int main(void)
{
    scanf("%d%d", &N, &M);
    for (int i = 0; i < N; i++)
    {
        for (int j = 0; j < M; j++)
        {
            scanf("%d", &arr[i][j]);
        }
    }

    printf("%d\n", sol(N - 1, M - 1));
    return 0;
}