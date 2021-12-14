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
	
	int i;
	int cnt;
	
	while(1)
	{
		cnt=0;
		scanf("%d",&N);
		if(N==0) break;
		for(i=N+1;i<=2*N;i++)
		{
			if(isPrime(i)) cnt++;
		}
		printf("%d\n",cnt);
	}
}