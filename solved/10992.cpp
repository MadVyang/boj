#include <stdio.h>

int main()
{
	int N,i,j;
	scanf("%d",&N);
	
	for(i=0;i<N;i++)
	{
		for(j=0;j<N-i-1;j++) printf(" ");
		if(i!=0)printf("*");
		if(i!=N-1) for(j=0;j<i*2-1;j++) printf(" ");
		else for(j=0;j<i*2-1;j++) printf("*");
		printf("*");
		printf("\n");
	}
}