#include <stdio.h>

int arr[505][505];
int memo[505][505];

int max(int a,int b)
{
	return a>b?a:b;
}

int main()
{
	int n;
	scanf("%d",&n);
	int i,j;
	
	for(i=0;i<n;i++)
	{
		for(j=0;j<=i;j++)
		{
			scanf("%d",&arr[i][j]);
		}
	}
	
	for(i=0;i<n;i++)
	{
		memo[n-1][i]=arr[n-1][i];
	}
	
	for(i=n-2;i>=0;i--)
	{
		for(j=0;j<=i;j++)
		{
			memo[i][j]=arr[i][j]+max(memo[i+1][j],memo[i+1][j+1]);
		}
	}
	
	printf("%d",memo[0][0]);
}