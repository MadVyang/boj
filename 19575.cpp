#include <stdio.h>

int N, x;

long long cal(long long before, int plus)
{
    return before * x + plus;
}

int main()
{
    scanf("%d%d", &N, &x);

    int A, tmp;
    long long r = 0;
    for (int i = 0; i < N + 1; i++)
    {
        scanf("%d%d", &A, &tmp);
        r = cal(r, A) % 1000000007;
        // printf("      %d\n", r);
    }
    printf("%lld\n", r);

    return 0;
}