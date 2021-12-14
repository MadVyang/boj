#include <stdio.h>

long long num[1000001];
char op[1000001];
int count = 0;

long long cal(long long a, long long b, char c)
{
    if (c == '+')
    {
        return a + b;
    }
    else if (c == '-')
    {
        return a - b;
    }
    else if (c == '*')
    {
        return a * b;
    }
    else if (c == '/')
    {
        return a / b;
    }
    else
    {
        return -1;
    }
}
int vs(char a, char b)
{
    int _a, _b;
    if (a == '*' || a == '/')
        _a = 1;
    else
        _a = 0;
    if (b == '*' || b == '/')
        _b = 1;
    else
        _b = 0;
    return _a - _b;
}

int main()
{
    scanf("%lld", &num[count++]);
    do
    {
        char c = getc(stdin);
        if (c == EOF || c == '\n')
            break;

        op[count] = c;
        scanf("%lld", &num[count++]);
        // printf("%lld%c%lld\n", num[count - 2], op[count - 1], num[count - 1]);
    } while (true);

    // printf("%d\n", count);

    int p = 0, q = count - 1;
    while (true)
    {
        if (p == q)
            break;

        long long a = cal(num[p], num[p + 1], op[p + 1]);
        long long b = cal(num[q - 1], num[q], op[q]);
        if (vs(op[p + 1], op[q]) == 1)
        {
            num[p + 1] = a;
            p++;
        }
        else if (vs(op[p + 1], op[q]) == -1)
        {
            num[q - 1] = b;
            q--;
        }
        else
        {
            if (a >= b)
            {
                num[p + 1] = a;
                p++;
            }
            else
            {
                num[q - 1] = b;
                q--;
            }
        }
        // printf("%lld %lld\n", num[p], num[q]);
    }
    printf("%lld\n", num[p]);
    return 0;
}