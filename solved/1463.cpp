#include <stdio.h>

int m[1000005];
int N;

int min(int a,int b)
{
    return a>b?b:a;
}

int sol(int n)
{
    if(n==3) return 1;
    if(n==2) return 1;
    if(n==1) return 0;
    if(m[n]) return m[n];

    if(n%6==0) m[n]=min(min(sol(n/2),sol(n/3)),sol(n-1))+1;
    else if(n%3==0) m[n]=min(sol(n/3),sol(n-1))+1;
    else if(n%2==0) m[n]=min(sol(n/2),sol(n-1))+1;
    else m[n]=sol(n-1)+1;

    return m[n];
}

int main()
{
    scanf("%d",&N);

    printf("%d",sol(N));

    return 0;
}
