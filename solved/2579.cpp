#include <stdio.h>

int arr[305];
int mem[305];

int max(int a, int b)
{
    return a > b ? a : b;
}

int main()
{
    int n;
    scanf("%d", &n);
    int i, j;

    for (i = 0; i < n; i++)
    {
        scanf("%d", &arr[i]);
    }

    if (n == 1)
    {
        printf("%d", arr[0]);
        return 0;
    }
    if (n == 2)
    {
        printf("%d", arr[0] + arr[1]);
        return 0;
    }

    mem[0] = arr[0];
    mem[1] = arr[1] + arr[0];
    mem[2] = arr[2] + max(arr[0], arr[1]);

    if (n == 3)
    {
        printf("%d", mem[2]);
        return 0;
    }

    for (i = 3; i < n; i++)
    {
        mem[i] = arr[i] + max(mem[i - 2], arr[i - 1] + mem[i - 3]);
    }

    printf("%d", mem[n - 1]);
    return 0;
}