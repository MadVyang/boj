#include <stdio.h>

int arr[1005];
int main()
{
	int C;
	int N,i;
	double sum,cnt;
	scanf("%d",&C);
	
	while(C)
	{
		C--;
		
		scanf("%d",&N);
		sum=0;
		cnt=0;
		for(i=0;i<N;i++)
		{
			scanf("%d",&arr[i]);
			sum+=arr[i];
		}
		sum/=N;
		for(i=0;i<N;i++)
		{
			if(arr[i]>sum)
			{
				cnt++;
			}
		}
		cnt/=N;
		cnt*=100;
		
		printf("%.3lf%%\n",cnt);
	}
}