#include <stdio.h>
int map[60][60];

int M,N,K;

void fill(int x,int y)
{
	if(map[y][x]!=1) return;
	map[y][x]=0;
	if(x>0) fill(x-1,y);
	if(x<M-1) fill(x+1,y);
	if(y>0) fill(x,y-1);
	if(y<N-1) fill(x,y+1);
}

int main()
{
	int T;
	scanf("%d",&T);
	
	int x,y;
	int i,j;
	int cnt;
	while(T--)
	{
		for(i=0;i<60;i++)
		{
			for(j=0;j<60;j++)
			{
				map[i][j]=0;
			}
		}
		
		scanf("%d%d%d",&M,&N,&K);
		for(j=0;j<K;j++)
		{
			scanf("%d%d",&x,&y);
			map[y][x]=1;
		}
		
		cnt=0;
		for(i=0;i<N;i++)
		{
			for(j=0;j<M;j++)
			{
				if(map[i][j]==1)
				{
					fill(j,i);
					cnt++;
				}
			}
		}
		for(i=0;i<N;i++)
		{
			for(j=0;j<M;j++)
			{
				//printf("%d ",map[i][j]);
			}
		//	printf("\n");
		}
		
		printf("%d\n",cnt);
	}
}