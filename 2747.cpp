#include <stdio.h>

int memo[100];

int fibo(int n)
{
	if(n==0) return 0;
	if(n==1) return 1;
	if(memo[n]) return memo[n];
	
	memo[n]=fibo(n-1)+fibo(n-2);
	return memo[n];
}

int main()
{
	int n;
	scanf("%d",&n);
	printf("%d",fibo(n));
}