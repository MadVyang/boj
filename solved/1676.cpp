#include <stdio.h>

int m[1005];

int main()
{
	int n,k;
	scanf("%d",&n);
	
	int i;
	int c=1;
	int cnt=0;
	for(i=1;i<=n;i++)
	{
		c*=i;
		c%=100000;
		
		while(c%10==0 && c>0)
		{
			cnt++;
			c/=10;
		}
		//printf("%d\n",c);
	}
	
	printf("%d",cnt);
}