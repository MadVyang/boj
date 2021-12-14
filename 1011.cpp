#include <stdio.h>

void my(int n)
{
	int r=0;
	int i=0;
	
	for(i=1;;i++)
	{
		if(n<=i)
		{
			r++;
			break;
		}
		else if(n<=i*2)
		{
			r+=2;
			break;
		}
		r+=2;
		n-=i*2;
	}
	
	printf("%d\n",r);
}

int main()
{
	int N,i,x,y;
	scanf("%d",&N);
	for(i=0;i<N;i++)
	{
		scanf("%d%d",&x,&y);
		my(y-x);
	}
}