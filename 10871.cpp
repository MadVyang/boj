#include <stdio.h>

int main()
{
	int N,X;
	int a;
	
	scanf("%d%d",&N,&X);
	
	int i;
	for(i=0;i<N;i++)
	{
		scanf("%d",&a);
		if(a<X) printf("%d ",a);
	}
}