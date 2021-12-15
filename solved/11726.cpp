#include <stdio.h>

int arr[1005];
int N;

int main()
{
	scanf("%d",&N);
	
	arr[0]=1; arr[1]=1; arr[2]=2;
	arr[3]=3; arr[4]=arr[3]+arr[2];
	
	int i,j;
	for(i=5;i<=N;i++)
	{
		arr[i]=arr[i-1]+arr[i-2];
		arr[i]%=10007;
	}
	printf("%d",arr[N]);
}