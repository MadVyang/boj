#include <stdio.h>

int N, M;
int S, E;
int arr[3000];
int ans[3000][3000];
bool check[3000][3000];

int sol(int a, int b)
{
    if (a == b)
        return 1;
    if (a > b)
        return 1;

    if (check[a][b])
        return ans[a][b];
    check[a][b] = true;

    if (arr[a] == arr[b] && sol(a + 1, b - 1) == 1)
    {
        ans[a][b] = 1;
        return ans[a][b];
    }
    return 0;
}

int main(void)
{
    scanf("%d", &N);
    for (int i = 1; i <= N; i++)
        scanf("%d", &arr[i]);

    scanf("%d", &M);
    for (int i = 0; i < M; i++)
    {
        scanf("%d%d", &S, &E);
        printf("%d\n", sol(S, E) == 1 ? 1 : 0);
    }
    return 0;
}