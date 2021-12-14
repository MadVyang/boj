#include <stdio.h>

int x, y, z;
int a, b, c;
int main()
{
    scanf("%d%d%d", &x, &y, &z);
    a = (x + y - z);
    b = (x + z - y);
    c = (y + z - x);
    if (a > 0 && b > 0 && c > 0 && a != 0 && b != 0 && c != 0)
    {
        printf("%d\n", 1);
        printf("%.1lf %.1lf %.1lf\n", a / 2.0, b / 2.0, c / 2.0);
    }
    else
    {
        printf("%d\n", -1);
    }
    return 0;
}