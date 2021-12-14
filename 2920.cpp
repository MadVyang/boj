#include <stdio.h>
int main()
{
	int i;
	int n,m;
	int chk;
	scanf("%d",&n);
	if(n==1) chk=0;
	else if(n==8) chk=1;
	else chk=-1;
	for(i=1;i<8;i++)
	{
		m=n;
		scanf("%d",&n);
		if(chk==0)
		{
			if(n-m!=1)
			{
				chk=-1;
				break;
			}
		}
		else if(chk==1)
		{
			if(n-m!=-1)
			{
				chk=-1;
				break;
			}
		}
	}
	if(chk==0) printf("ascending");
	else if(chk==1) printf("descending");
	else printf("mixed");
}