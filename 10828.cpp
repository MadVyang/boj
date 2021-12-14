#include <stdio.h>

int main()
{
	int stack[10005];
	
	int n;
	scanf("%d",&n);
	
	int i;
	char tmp[20];
	int k;
	
	int cnt=0;
	
	for(i=0;i<n;i++)
	{
		scanf("%s",&tmp);
		if(tmp[0]=='p' && tmp[1]=='u')
		{
			scanf("%d",&k);
			stack[cnt]=k;
			cnt++;
		}
		else if(tmp[0]=='p' && tmp[1]=='o')
		{
			if(cnt==0) printf("-1\n");
			else if(cnt>0)
			{
				cnt--;
				printf("%d\n",stack[cnt]);
				stack[cnt]=0;
			}
		}	
		else if(tmp[0]=='s')
		{
			printf("%d\n",cnt);
		}	
		else if(tmp[0]=='e')
		{
			printf("%d\n",cnt==0?1:0);
		}
		else
		{
			if(cnt==0) printf("-1\n");
			else if(cnt>0)
			{
				printf("%d\n",stack[cnt-1]);
			}
		}
	}
}