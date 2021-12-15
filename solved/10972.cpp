#include <stdio.h>
#include <algorithm>
#include <iostream>

using namespace std;

int N;
int A[10001];

int factorial(int n)
{
    if (n == 1)
        return 1;
    return n * factorial(n - 1);
}

int toInteger()
{
    int r = 0;
    for (int i = 0; i < N; i++)
    {
        r *= 10;
        r += A[i];
    }
    return r;
}
void printArr()
{
    for (int i = 0; i < N; i++)
    {
        printf("%d ", A[i]);
    }
    printf("\n");
}

void swap(int a, int b)
{
    int tmp = A[a];
    A[a] = A[b];
    A[b] = tmp;
}

int find(int index)
{
    int min = N + 1;
    int r = -1;
    for (int i = index + 1; i < N; i++)
    {
        if (A[i] > A[index] && A[i] < min)
        {
            min = A[i];
            r = i;
        }
    }
    return r;
}

bool check(int index)
{
    for (int i = index + 1; i < N; i++)
    {
        if (A[i] > A[index])
            return true;
    }
    return false;
}

void carry(int index)
{
    if (check(index))
    {
        int target = find(index);
        // cout << "test  " << A[index] << "  " << A[target] << endl;
        swap(index, target);
        sort(A + index + 1, A + N);
    }
    else
    {
        carry(index - 1);
    }
}

void next()
{
    int before = toInteger();
    swap(N - 2, N - 1);
    int after = toInteger();

    if (before > after)
    {
        carry(N - 3);
    }
}

int main()
{
    scanf("%d", &N);
    for (int i = 0; i < N; i++)
    {
        scanf("%d", A + i);
    }

    // for (int i = 0; i < factorial(N); i++)
    // {
    //     printf("%4d:   ", i + 1);
    //     printArr();

    //     next();
    // }
    // printf("%4d:   ", factorial(N) + 1);

    next();
    if (A[0] != 0)
    {
        printArr();
    }
    else
    {
        printf("-1\n");
    }

    return 0;
}