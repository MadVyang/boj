#include <stdio.h>
int main()
{
	int N,i,j;
	scanf("%d",&N);
	
	for(i=N;i>0;i--)
	{
		for(j=0;j<N-i;j++)
		{
			printf(" ");
		}
		for(j=0;j<i*2-1;j++) printf("*");
		for(j=0;j<N-i;j++)
		{
			//printf(" ");
		}
		printf("\n");
	}
	for(i=2;i<=N;i++)
	{
		for(j=0;j<N-i;j++)
		{
			printf(" ");
		}
		for(j=0;j<i*2-1;j++) printf("*");
		for(j=0;j<N-i;j++)
		{
			//printf(" ");
		}
		printf("\n");
	}
}