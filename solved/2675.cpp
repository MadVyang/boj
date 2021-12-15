#include <stdio.h>
#include <string.h>
int main()
{
	int N;
	scanf("%d",&N);
	
	int a,i,j;
	char s[100];
	while(N--)
	{
		scanf("%d %s",&a,&s);
		
		for(i=0;i<strlen(s);i++)
		{
			for(j=0;j<a;j++)
			{
				printf("%c",s[i]);
			}
		}
		printf("\n");
	}
}