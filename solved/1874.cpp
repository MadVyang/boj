#include <stdio.h>

int list[100005];
int chk[100005];

int main()
{
	int N;
	scanf("%d",&N);
	
	int i,j;
	int p=0;
	for(i=0;i<N;i++)
	{
		scanf("%d",&list[i]);
	}
	
	p=1;
	for(i=0;i<N;i++)
	{
		for(;p<=list[i];p++)
		{
			if(chk[p]==0)
			{
				chk[p]=1;
			}
		}
		for(j=0;p==list[i-j]+1;j++)
		{
			chk[p-1]=-1;
			while(chk[p-1]==-1) p--;
		}
		if(i!=N-1 && list[i]>list[i+1])
		{
			for(j=list[i+1]+1;j<list[i];j++)
			{
				if(chk[j]==1)
				{
					printf("NO\n");
					return 0;
				}
			}
		}
	}
	//////
	
	for(i=0;i<100005;i++) chk[i]=0;
	p=1;
	for(i=0;i<N;i++)
	{
		for(;p<=list[i];p++)
		{
			if(chk[p]==0)
			{
				chk[p]=1;
				//printf("push %d\n",p);
				printf("+\n");
			}
		}
		for(j=0;p==list[i-j]+1;j++)
		{
			chk[p-1]=-1;
			if(p-1>0)
			{
				//printf("pop %d\n",p-1);
				printf("-\n");
			}
			while(chk[p-1]==-1) p--;
		}
	}
}