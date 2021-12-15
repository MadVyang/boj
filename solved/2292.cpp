#include <stdio.h>

int main()
{
	int N;
	scanf("%d",&N);
	
	N--;
	int cnt=1;
	while(N>0)
	{
		N-=6*cnt;
		cnt++;
	}
	
	printf("%d",cnt);
	
	return 0;
}