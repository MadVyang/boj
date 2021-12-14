#include <stdio.h>

int T,A,B;
int main()
{
    scanf("%d",&T);
    int i;
    for(i=0;i<T;i++)
    {
        scanf("%d,%d",&A,&B);
        printf("%d\n",(A+B));
    }
    return 0;
}