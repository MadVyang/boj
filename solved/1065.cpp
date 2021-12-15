#include <stdio.h>

int chk(int n)
{
	int a,b;
	int num=10;
	while(n)
	{
		if(n<10) break;
		a=n%10;
		n/=10;
		b=n%10;
		if(num==a-b || num==10)
		{
			num=a-b;
		}
		else
		{
			//printf("\n\n\n\n%d %d",num,a-b);
			return 0;
		}
	}
	
	return 1;
}

int N;
int main()
{
	scanf("%d",&N);
	int i,sum=0;
	for(i=1;i<=N;i++)
	{
		if(chk(i)) sum++;
	}
	printf("%d",sum);
}