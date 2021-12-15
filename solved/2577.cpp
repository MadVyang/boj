#include <stdio.h>

int arr[20];
int a,b,c;
int main()
{
	scanf("%d%d%d",&a,&b,&c);
	int X=a*b*c;
	
	while(X)
	{
		arr[X%10]++;
		X/=10;
	}
	
	int i;
	for(i=0;i<=9;i++)
	{
		printf("%d\n",arr[i]);
	}
}