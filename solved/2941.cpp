#include <stdio.h>
#include <string.h>
int main()
{
	char str[105];
	scanf("%s",&str);
	
	int sum=0,i;
	for(i=0;i<strlen(str);i++)
	{
		if(str[i]=='c')
		{
			if(str[i+1]=='=' ||
			   str[i+1]=='-' ) sum++;
		}
		if(str[i]=='d')
		{
			if(str[i+1]=='-') sum++;
			else if(str[i+1]=='z' && str[i+2]=='=')
			{
				sum+=2;
				i+=2;
				continue;
			}
		}
		if(str[i]=='l')
		{
			if(str[i+1]=='j') sum++;
		}
		if(str[i]=='n')
		{
			if(str[i+1]=='j') sum++;
		}
		if(str[i]=='s')
		{
			if(str[i+1]=='=') sum++;
		}
		if(str[i]=='z')
		{
			if(str[i+1]=='=') sum++;
		}
	}
	printf("%d",strlen(str)-sum);
	return 0;
}