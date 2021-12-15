#include <stdio.h>

int n;

int main()
{
	int i;
	char c;
	int sum=0;
	scanf("%d\n",&n);
	for(i=0;i<n;i++)
	{
		scanf("%c",&c);
		sum+=c-'0';
	}
	printf("%d",sum);
}