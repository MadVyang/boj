#include <stdio.h>

int map[1030][2050];

void draw(int y,int x,int n)
{
	if(n==1)
	{
		map[y][x]='*';
		return;
	}
	
	int i;
	int H=1,W=1;
	for(i=1;i<n;i++)
	{
		H=2*H+1;
		W=2*W+3;
	}
	
	int Y,X;
	if(n%2==1)
	{
		Y=y;
		X=x+W/2;
		
		for(i=1;i<H;i++)
		{
			map[Y][X]='*';
			Y++;
			X--;
		}
		for(i=1;i<W;i++)
		{
			map[Y][X]='*';
			X++;
		}
		for(i=1;i<H;i++)
		{
			map[Y][X]='*';
			Y--;
			X--;
		}
	}
	else
	{
		Y=y;
		X=x;
		
		for(i=1;i<H;i++)
		{
			map[Y][X]='*';
			Y++;
			X++;
		}
		for(i=1;i<H;i++)
		{
			map[Y][X]='*';
			Y--;
			X++;
		}
		for(i=1;i<W;i++)
		{
			map[Y][X]='*';
			X--;
		}
	}
	
	draw(y+(n%2?H/2:1),x+W/4+1,n-1);
}

int main()
{
	int N,i,j;
	scanf("%d",&N);
	
	draw(0,0,N);
	
	int H=1,W=1;
	for(i=1;i<N;i++)
	{
		H=2*H+1;
		W=2*W+3;
	}
	for(i=0;i<H;i++)
	{
		if(N%2==1)
		{
			for(j=0;j<W-H+i+1;j++)
			{
				printf("%c",map[i][j]?map[i][j]:' ');
			}
			printf("\n");
		}
		else
		{
			for(j=0;j<W-i;j++)
			{
				printf("%c",map[i][j]?map[i][j]:' ');
			}
			printf("\n");
		}
	}
}