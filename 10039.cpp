#include <stdio.h>
int main()
{
	int i,a,sum=0;
	for(i=0;i<5;i++)
	{
		scanf("%d",&a);
		if(a<40) a=40;
		sum+=a;
	}
	printf("%d",sum/5);
}