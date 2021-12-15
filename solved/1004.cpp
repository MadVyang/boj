#include <stdio.h>

int main()
{
	int T;
	scanf("%d",&T);
	
	int x1,y1,x2,y2,n,cx,cy,r;
	int i;
	int dis1,dis2,R;
	int cnt;
	while(T--)
	{
		scanf("%d%d%d%d",&x1,&y1,&x2,&y2);
		scanf("%d",&n);
		
		cnt=0;
		for(i=0;i<n;i++)
		{
			scanf("%d%d%d",&cx,&cy,&r);
			dis1=(x1-cx)*(x1-cx)+(y1-cy)*(y1-cy);
			dis2=(x2-cx)*(x2-cx)+(y2-cy)*(y2-cy);
			R=r*r;
			
			if(dis1<R && dis2<R)
			{
			}
			else if(dis1<R || dis2<R) cnt++;
		}
		printf("%d\n",cnt);
	}
}