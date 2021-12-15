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
		if(i>1)printf("\n");
	}
}