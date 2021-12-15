#include <stdio.h>
#include <string.h>

char str[1000001];

int main()
{
	gets(str);
	int i=0;
	char c=' ';
	int cnt=0;
	int max=strlen(str);
	for(;i<max;i++)
	{
		if(c=='\0' || c=='\n') break;
		c=str[i];
		if(c!=' ')
		{
			while(c!=' ' && i<max)
			{
				i++;
				c=str[i];
			}
			cnt++;
		}
	}
	printf("%d",cnt);
	return 0;
}