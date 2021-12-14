#include <stdio.h>
int map[505][505];
int mem[505][505]={-1};
int chk[505][505];
int M,N;

int sol(int y,int x)
{
	//printf("%d %d\n",x+1,y+1);
	if(y==0 && x==0) return 1;
	if(mem[y][x]!=-1) return mem[y][x];
	
	int r=0;
	if(y>0 && map[y-1][x]>map[y][x])
	{
		r+=sol(y-1,x);
	}
	if(x>0 && map[y][x-1]>map[y][x])
	{
		r+=sol(y,x-1);
	}
	if(y<M-1 && map[y+1][x]>map[y][x])
	{
		r+=sol(y+1,x);
	}
	if(x<N-1 && map[y][x+1]>map[y][x])
	{
		r+=sol(y,x+1);
	}
	
	mem[y][x]=r;
	
	return r;
}

int main()
{
	int i,j;
	
	scanf("%d%d",&M,&N);
	for(i=0;i<M;i++)
	{
		for(j=0;j<N;j++)
		{
			scanf("%d",&map[i][j]);
			mem[i][j]=-1;
		}
	}
	
	sol(M-1,N-1);
	
	for(i=0;i<M;i++)
	{
		for(j=0;j<N;j++)
		{
		//	printf("%d ",mem[i][j]);
		}
		//printf("\n");
	}
	
	printf("%d",mem[M-1][N-1]);
}