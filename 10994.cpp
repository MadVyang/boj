#include <stdio.h>

int map[500][500];

void draw(int y,int x,int n)
{
	map[y][x]='*';
	if(n==1) return;
	int i;
	for(i=1;i<n;i++)
	{
		y++;
		map[y][x]='*';
	}
	for(i=1;i<n;i++)
	{
		x++;
		map[y][x]='*';
	}
	for(i=1;i<n;i++)
	{
		y--;
		map[y][x]='*';
	}
	for(i=1;i<n;i++)
	{
		x--;
		map[y][x]='*';
	}
	
	draw(y+2,x+2,n-4);
}

int main()
{
	int N,i,j;
	scanf("%d",&N);
	
	draw(0,0,(N-1)*4+1);
	
	for(i=0;i<(N-1)*4+1;i++)
	{
		for(j=0;j<(N-1)*4+1;j++)
		{
			printf("%c",map[i][j]?map[i][j]:' ');
		}
		printf("\n");
	}
}