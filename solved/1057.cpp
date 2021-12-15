#include <stdio.h>
int main()
{
	int N,a,b;
	scanf("%d%d%d",&N,&a,&b);
	
	int cnt=0;
	while(a!=b)
	{
		a=(a+1)/2;
		b=(b+1)/2;
		cnt++;
	}
	printf("%d\n",cnt);
}