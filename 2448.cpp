#include <stdio.h>

char arr[10000][10000];

int sqrt2(int n)
{
	int cnt=0;
	while(n/=2) cnt++;
	return cnt;
}

void my(int y,int x,int n)
{
	int i;
	if(n>0)
	{
		my(y,x,n-1);
		my(y+(1<<(n-1))*3,x-(1<<(n-1))*3,n-1);
		my(y+(1<<(n-1))*3,x+(1<<(n-1))*3,n-1);
	}
	else if(n==0)
	{
		arr[y][x]='*';
		arr[y+1][x-1]='*';
		arr[y+1][x+1]='*';
		for(i=0;i<5;i++)
		{
			arr[y+2][x-2+i]='*';
		}
	}
}

int main()
{
	int i,j;
	//
	
	int in;
	scanf("%d",&in);
	
	int N=sqrt2(in/3);
	int size=(1<<(N))*3-1;
	
	for(i=0;i<size+1;i++)
	{
		for(j=0;j<size*2+3;j++) arr[i][j]=' ';
	}
	
	my(0,size,N);
	
	for(i=0;i<size+1;i++)
	{
		if(i<size)
		{
			for(j=0;j<size*2+3;j++) printf("%c",arr[i][j]);
			printf("\n");
		}
		else for(j=0;j<size*2+2;j++) printf("%c",arr[i][j]);
	}
	
	return 0;
}