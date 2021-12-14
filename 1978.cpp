#include <stdio.h>

int isPrime(int n)
{
	if(n==1) return 0;
	int i;
	for(i=2;i*i<=n;i++)
	{
		if(n%i==0) return 0;
	}
	return 1;
}
int main()
{
	int N;
	scanf("%d",&N);
	
	int i,cnt=0,tmp;
	for(i=0;i<N;i++)
	{
		scanf("%d",&tmp);
		if(isPrime(tmp)) cnt++;
	}
	printf("%d",cnt);
}