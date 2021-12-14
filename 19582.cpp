#include <stdio.h>

int N;
int arr[100002][2];

int check(int ex, int count)
{
    if (count > 1)
        return 0;

    int max = -1;
    int index = 0;

    int sum = 0;
    for (int i = 0; i < N; i++)
    {
        if (i == ex)
            continue;
        if (sum > arr[i][0])
        {
            int a = check(index, count + 1);
            int b = check(i, count + 1);
            return a > b ? a : b;
        }
        else
        {
            if (max < arr[i][1])
            {
                max = arr[i][1];
                index = i;
            }
            sum += arr[i][1];
        }
    }
    return 1;
}

int main()
{
    scanf("%d", &N);
    for (int i = 0; i < N; i++)
    {
        scanf("%d%d", &arr[i][0], &arr[i][1]);
    }
    if (check(-1, 0))
    {
        printf("Kkeo-eok\n");
    }
    else
    {
        printf("Zzz\n");
    }
    return 0;
}