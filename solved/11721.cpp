#include <stdio.h>
#include <string.h>

char str[105];

int main()
{
	int i;
	scanf("%s",&str);
	for(i=0;i<strlen(str);i++)
	{
		printf("%c",str[i]);
		if((i+1)%10==0) printf("\n");
	}
}