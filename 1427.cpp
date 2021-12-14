#include <stdio.h>
#include <algorithm>

int N;
int arr[20];
int main()
{
	scanf("%d",&N);
	
	if(N==0) printf("0");
	int i=0;
	while(N)
	{
		arr[i]=N%10;
		N/=10;
		i++;
	}
	
	std::sort(arr,arr+i);
	
	int j;
	for(j=i-1;j>=0;j--)
		printf("%d",arr[j]);
	printf("\n");
}