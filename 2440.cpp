#include <stdio.h>

int main()
{
	int i,j;
	int n;
	scanf("%d",&n);
	for(i=n;i>0;i--)
	{
		for(j=0;j<i;j++)
		{
			printf("*");
		}
		if(i==1) break;
		printf("\n");
	}
	return 0;
}