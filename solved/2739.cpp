#include <stdio.h>

int N;
int main()
{
	int i;
	scanf("%d",&N);
	for(i=1;i<=9;i++) printf("%d * %d = %d\n",N,i,N*i);
}

