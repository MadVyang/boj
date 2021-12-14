#include <stdio.h>

int map[2200][2200];

void draw(int y,int x,int size)
{
	if(size>3)
	{
		draw(y,x,size/3);
		draw(y,x+size/3,size/3);
		draw(y,x+size/3*2,size/3);
		draw(y+size/3,x,size/3);
		draw(y+size/3,x+size/3*2,size/3);
		draw(y+size/3*2,x,size/3);
		draw(y+size/3*2,x+size/3,size/3);
		draw(y+size/3*2,x+size/3*2,size/3);
	}
	else
	{
		map[y][x]='*';
		map[y][x+1]='*';
		map[y][x+2]='*';
		map[y+1][x]='*';
		map[y+1][x+2]='*';
		map[y+2][x]='*';
		map[y+2][x+1]='*';
		map[y+2][x+2]='*';
	}
}

int main()
{
	int N,i,j;
	scanf("%d",&N);
	
	draw(0,0,N);
	
	for(i=0;i<N;i++)
	{
		for(j=0;j<N;j++)
		{
			if(map[i][j]) printf("%c",map[i][j]);
			else printf(" ");
		}
		printf("\n");
	}
}