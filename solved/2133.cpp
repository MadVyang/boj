#include <stdio.h>

int arr[300];
int N;

int main()
{
	scanf("%d",&N);
	
	arr[0]=1; arr[1]=0; arr[2]=3;
	arr[3]=0; arr[4]=arr[2]*3+2;
	
	int i,j;
	for(i=5;i<=N;i++)
	{
		if(i%2) arr[i]=0;
		else arr[i]=arr[i-2]*3;
		for(j=4;i-j>=0;j+=2)
		{
			arr[i]+=arr[i-j]*2;
		}
	}
	printf("%d",arr[N]);
}