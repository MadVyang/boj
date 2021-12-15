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
	int T,N;
	
	scanf("%d",&T);
	int i;
	int tmp;
	for(i=0;i<T;i++)
	{
		scanf("%d",&N);
		tmp=N/2;
		for(;tmp>=2;tmp--)
		{
			if(isPrime(tmp)&&isPrime(N-tmp))
			{
				printf("%d %d\n",tmp,N-tmp);
				break;
			}
		}
	}
}