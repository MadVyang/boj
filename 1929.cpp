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
	int M,N;
	scanf("%d%d",&M,&N);
	
	int i,sum=0,tmp,min=-1;
	for(i=M;i<=N;i++)
	{
		if(isPrime(i))
		{
			printf("%d\n",i);
		}
	}
	/*
	if(min==-1) printf("-1");
	else printf("%d\n%d",sum,min);*/
}