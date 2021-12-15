#include <stdio.h>

int main()
{
	int N,i,j;
	scanf("%d",&N);
	
	for(i=0;i<N;i++)
	{
		if(i%2) printf(" ");
		printf("*");
		for(j=1;j<N;j++) printf(" *");
		printf("\n");
	}
}