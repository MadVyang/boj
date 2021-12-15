#include <stdio.h>

int T,A,B;
int main()
{
    scanf("%d",&T);
    int i;
    for(i=0;i<T;i++)
    {
        scanf("%d%d",&A,&B);
        printf("Case #%d: %d\n",i+1,(A+B));
    }
    return 0;
}