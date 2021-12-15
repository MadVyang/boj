#include <stdio.h>

int main()
{
	int N,i,j;
	scanf("%d",&N);
	
	if(N==1) printf("*\n");
	else
	{
		for(i=0;i<N*2;i++)
		{
			if(i%2) printf(" ");
			printf("*");
			if(N%2) for(j=1;j<N/2+((i+1)%2);j++) printf(" *");
			else for(j=1;j<N/2+((N)%2);j++) printf(" *");
			printf("\n");
		}
	}
}