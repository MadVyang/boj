#include <stdio.h>


int N;
int arr[10005];
int main()
{
	scanf("%d",&N);
	int i;
	int tmp;
	for(i=0;i<N;i++)
	{
		scanf("%d",&tmp);
		arr[tmp]++;
	}
	
	for(i=0;i<=10000;i++)
	{
		while(arr[i])
		{
			printf("%d\n",i);
			arr[i]--;
		}
	}
}