#include <stdio.h>

unsigned long long memo[100];

unsigned long long fibo(unsigned long long n)
{
	if(n==0) return 0;
	if(n==1) return 1;
	if(memo[n]) return memo[n];
	
	memo[n]=fibo(n-1)+fibo(n-2);
	return memo[n];
}

int main()
{
	unsigned long long n;
	scanf("%llu",&n);
	printf("%llu",fibo(n));
}