#include <stdio.h>

int main()
{
	int N,i,H,W,a;
	scanf("%d",&N);
	for(i=0;i<N;i++)
	{
		scanf("%d%d%d",&H,&W,&a);
		if(a%H) printf("%d\n",a%H*100+a/H+1);
		else printf("%d\n",H*100+a/H);
	}
}