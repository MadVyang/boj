#include <stdio.h>

int main()
{
	int T;
	scanf("%d",&T);
	
	int a,b;
	int i;
	
	int tmp;
	for(i=0;i<T;i++)
	{
		scanf("%d%d",&a,&b);
		tmp=1;
		
		while(b--)
		{
			tmp*=a;
			tmp%=10;
		}
		printf("%d\n",tmp==0?10:tmp);
	}
}