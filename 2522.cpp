#include <stdio.h>

int main()
{
	int N,i,j;
	scanf("%d",&N);
	
	for(i=0;i<N;i++)
	{
		for(j=0;j<N-i-1;j++) printf(" ");
		for(j=0;j<i+1;j++) printf("*");
		printf("\n");
	}
	
	for(i=N-2;i>=0;i--)
	{
		for(j=0;j<N-i-1;j++) printf(" ");
		for(j=0;j<i+1;j++) printf("*");
		printf("\n");
	}
}