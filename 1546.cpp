#include <stdio.h>

int arr[1005];
int main()
{
	int N;
	
	scanf("%d",&N);
	
	int i;
	
	for(i=0;i<N;i++)
	{
		scanf("%d",&arr[i]);
	}
	int max=-1;
	for(i=0;i<N;i++)
	{
		if(arr[i]>max) max=arr[i];
	}
	double sum=0;
	for(i=0;i<N;i++)
	{
		sum+=(double)arr[i]/max*100;
	}
	sum/=N;
	printf("%.2lf",sum);	
}