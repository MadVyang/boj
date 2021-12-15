#include <stdio.h>

int main()
{
	char c;
	for(; ;)
	{
		c='\0';
		scanf("%c",&c);
		if(c=='\0') break;
		else printf("%c",c);
	}
	return 0;
}