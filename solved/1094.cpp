#include <stdio.h>

int main()
{
	int N;
	scanf("%d",&N);
	
	int cnt=0;
	while(N)
	{
		if(N%2) cnt++;
		N/=2;
	}
	printf("%d",cnt);
}