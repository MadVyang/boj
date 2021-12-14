#include <stdio.h>
#include <string.h>

char s[100];
int main()
{
	int j,N;
	scanf("%d",&N);
	while(N--)
	{
		scanf("%s",&s);
		int i;
		int sum=0;
		int cnt=0;
		for(i=0;i<strlen(s);i++)
		{
			cnt=0;
			while(s[i]=='O')
			{
				cnt++;
				sum+=cnt;
				i++;
			}
		}
		printf("%d\n",sum);
	}
}