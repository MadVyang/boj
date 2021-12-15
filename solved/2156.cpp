#include <stdio.h>

int arr[10005];
int mem[10005];

int max(int a,int b)
{
	return a>b?a:b;
}

int main()
{
	int N;
	scanf("%d",&N);
	
	int i;
	for(i=0;i<N;i++)
	{
		scanf("%d",&arr[i]);
	}
	
	mem[0]=arr[0];
	mem[1]=arr[0]+arr[1];
	mem[2]=arr[2]+max(arr[0],arr[1]);
	mem[3]=arr[3]+max(arr[0]+arr[2],arr[0]+arr[1]);
	
	for(i=4;i<N;i++)
	{
		mem[i]=arr[i]+max(max(mem[i-2],arr[i-1]+mem[i-3]),arr[i-1]+mem[i-4]);
	}
	
	int M=0;
	for(i=0;i<N;i++)
	{
		if(M<mem[i]) M=mem[i];
	}
	printf("%d",M);
}