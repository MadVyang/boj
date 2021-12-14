#include <stdio.h>

int m[1005];

int f(int n)
{
	if(n==0) return 1;
	if(n==1) return 1;
	return f(n-1)*n;
}

int main()
{
	int n,k;
	scanf("%d",&n);
	
	printf("%d",f(n));
}