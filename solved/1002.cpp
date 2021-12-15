#include <stdio.h>

int main()
{
	int T;
	scanf("%d",&T);
	
	int i;
	int x1,y1,x2,y2,r1,r2;
	for(i=0;i<T;i++)
	{
		scanf("%d%d%d%d%d%d",&x1,&y1,&r1,&x2,&y2,&r2);
		
		int dis=(x1-x2)*(x1-x2)+(y1-y2)*(y1-y2);
		int r=(r1+r2)*(r1+r2);
		
		if(x1==x2 && y1==y2 && r1==r2)
		{
			printf("-1\n");
		}
		
		else if (dis==r)
		{
			printf("1\n");
		}
		else if(dis>r) printf("0\n");
		else
		{
			if((r1-r2)*(r1-r2)==dis) printf("1\n");
			else if((r1-r2)*(r1-r2)>dis) printf("0\n");
			else printf("2\n");
		}
	}
}