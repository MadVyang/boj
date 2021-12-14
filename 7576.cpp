#include <stdio.h>
#include <stdlib.h>

int map[1002][1002];
int next[1002][1002];
int chk[1002][1002];
int M,N;

struct node
{
	int y;
	int x;
	char old;
	struct node *next;
};
typedef struct node list;

list* head=NULL;
list* tail=NULL;

void add(int y,int x)
{
	if(chk[y][x]) return;
	
	list* tmp;
	if(head==NULL)
	{
		head=(list*)malloc(sizeof(list));
		head->y=y;
		head->x=x;
		head->old=0;
		head->next=NULL;
		tail=head;
	}
	else
	{
		tmp=(list*)malloc(sizeof(list));
		tmp->y=y;
		tmp->x=x;
		tmp->old=0;
		tmp->next=NULL;
		tail->next=tmp;
		tail=tmp;
	}
	
	chk[y][x]=1;
}

void find(int y,int x)
{
	if(y>0 && map[y-1][x]==0) add(y-1,x);
	if(x>0 && map[y][x-1]==0) add(y,x-1);
	if(y<N-1 && map[y+1][x]==0) add(y+1,x);
	if(x<M-1 && map[y][x+1]==0) add(y,x+1);
}

int main()
{
	scanf("%d%d",&M,&N);
	int i,j;
	for(i=0;i<N;i++)
	{
		for(j=0;j<M;j++)
		{
			scanf("%d",&map[i][j]);
		}
	}
	for(i=0;i<N;i++)
	{
		for(j=0;j<M;j++)
		{
			if(map[i][j]==1) find(i,j);
		}
	}
	int cnt=0;
	int finished=1;
	while(1)
	{
		if(head==NULL)
		{
			finished=1;
			for(i=0;i<N;i++)
			{
				for(j=0;j<M;j++)
				{
					if(map[i][j]==0) finished=0;
				}
			}
			if(finished) printf("%d",cnt);
			else printf("-1");
			return 0;
		}
		
		list* tmp;
		for(tmp=head;tmp!=NULL;tmp=tmp->next)
		{
			map[tmp->y][tmp->x]=1;
			tmp->old=1;
		}

		for(tmp=head;tmp!=NULL&&tmp->old==1;tmp=tmp->next)
		{
			find(tmp->y,tmp->x);
		}
		for(tmp=head;tmp!=NULL&&tmp->old==1;tmp=tmp->next)
		{
			head=NULL;
			if(tmp->next!=NULL&&tmp->next->old==0)
			{
				head=tmp->next;
			}
		}
		/*
		
		for(i=0;i<N;i++)
		{
			for(j=0;j<M;j++)
			{
				printf("%d ",map[i][j]);
			}
			printf("\n");
		}
		printf("\n");
		*/
		cnt++;
	}
}