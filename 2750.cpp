#include <stdio.h>

int N;
int arr[2004];
int main()
{
	scanf("%d",&N);
	int i;
	int tmp;
	for(i=0;i<N;i++)
	{
		scanf("%d",&tmp);
		arr[tmp+1000]=1;
	}
	
	for(i=-1000;i<1001;i++)
	{
		if(arr[i+1000]) printf("%d\n",i);
	}
}