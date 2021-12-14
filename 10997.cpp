#include <stdio.h>

int map[1000][1000];

void draw(int y,int x,int n)
{
	int i;
	map[y][x]='*';
	if(n==1)
	{
		return;
	}
	if(n==2)
	{
		for(i=0;i<(n-1)*4;i++)
		{
			x--;
			map[y][x]='*';
		}
		for(i=0;i<(n-1)*4+2;i++)
		{
			y++;
			map[y][x]='*';
		}
		for(i=0;i<(n-1)*4;i++)
		{
			x++;
			map[y][x]='*';
		}
		for(i=0;i<(n-1)*4;i++)
		{
			y--;
			map[y][x]='*';
		}
		map[y][x-1]='*';
		map[y][x-2]='*';
		map[y+1][x-2]='*';
		map[y+2][x-2]='*';
		
		return;
	}
	
	for(i=0;i<(n-1)*4;i++)
	{
		x--;
		map[y][x]='*';
	}
	for(i=0;i<(n-1)*4+2;i++)
	{
		y++;
		map[y][x]='*';
	}
	for(i=0;i<(n-1)*4;i++)
	{
		x++;
		map[y][x]='*';
	}
	for(i=0;i<(n-1)*4;i++)
	{
		y--;
		map[y][x]='*';
	}
	map[y][x-1]='*';
	draw(y,x-2,n-1);
}

int main()
{
	int N,i,j;
	scanf("%d",&N);
	if(N==1)
	{
		printf("*\n");
		return 0;
	}
	draw(0,(N-1)*4,N);
	
	for(i=0;i<=(N-1)*4+2;i++)
	{
		if(i!=1)
		{
			for(j=0;j<=(N-1)*4;j++)
			{
				printf("%c",map[i][j]?map[i][j]:' ');
			}
		}
		else printf("*");
		printf("\n");
	}
}