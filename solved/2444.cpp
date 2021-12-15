#include <stdio.h>

int main()
{
	int i,j;
	int n;
	scanf("%d",&n);
	for(i=0;i<n;i++)
	{
		for(j=1;j<n-i;j++)
		{
			printf(" ");
		}
		for(j=0;j<=i*2;j++)
		{
			printf("*");
		}
		printf("\n");
	}
	for(i=n-2;i>=0;i--)
	{
		for(j=1;j<n-i;j++)
		{
			printf(" ");
		}
		for(j=0;j<=i*2;j++)
		{
			printf("*");
		}
		printf("\n");
	}
	return 0;
}