#include <stdio.h>

int my(int k,int n)
{
	if(k==0) return n;
	int r=0;
	int i;
	for(i=1;i<=n;i++)
	{
		r+=my(k-1,i);
	}
	return r;
}

int main()
{
	int N,i,k,n;
	scanf("%d",&N);
	for(i=0;i<N;i++)
	{
		scanf("%d%d",&k,&n);
		printf("%d\n",my(k,n));
	}
}