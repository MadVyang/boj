#include <stdio.h>
#include <string.h>

int main()
{
	int N;
	scanf("%d",&N);
	
	char str[100];
	
	int i;
	int chk;
	while(N--)
	{
		scanf("%s",&str);
		
		chk=0;
		for(i=0;i<strlen(str);i++)
		{
			if(str[i]=='(') chk++;
			else chk--;
			
			if(chk<0)
			{
				chk=-999999999;
				break;
			}
		}
		
		if(chk==0) printf("YES\n");
		else printf("NO\n");
	}
}