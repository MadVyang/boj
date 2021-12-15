#include <stdio.h>

int main()
{
	int N;
	scanf("%d",&N);
	
	int stat=0,cnt=1;
	while(stat+cnt<N)
	{
		stat+=cnt;
		cnt++;
	}
	
	if(cnt%2==1) printf("%d/%d",cnt-(N-stat)+1,N-stat);
	else printf("%d/%d",(N-stat),cnt-(N-stat)+1);
	
	return 0;
}