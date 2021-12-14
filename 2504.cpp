#include <stdio.h>
#include <string.h>

char str[50];

int cal(int x,int y)
{
	int i,chk;
	
	if(x>=y) return 0;
	if(str[x]=='(')
	{
		if(str[x+1]==')') return 2+cal(x+2,y);
		else
		{
			chk=1;
			for(i=x+1;i<=y;i++)
			{
				if(str[i]==')') chk--;
				if(str[i]=='(') chk++;
				
				if(chk==0)
				{
					return 2*cal(x+1,i-1)+cal(i+1,y);
				}
			}
		}
	}
	else if(str[x]=='[')
	{
		if(str[x+1]==']') return 3+cal(x+2,y);
		else
		{
			chk=1;
			for(i=x+1;i<=y;i++)
			{
				if(str[i]==']') chk--;
				if(str[i]=='[') chk++;
				
				if(chk==0)
				{
					return 3*cal(x+1,i-1)+cal(i+1,y);
				}
			}
		}
	}
	return -1;
}

int main()
{
	scanf("%s",&str);
	
	int a=0,b=0,i;
	for(i=0;i<strlen(str);i++)
	{
		if(str[i]=='(') a++;
		if(str[i]==')') a--;
		if(str[i]=='[') b++;
		if(str[i]==']') b--;
		
		if(a<0 || b<0)
		{
			printf("0\n");
			return 0; 
		}
	}
	
	if(a!=0 || b!=0)
	{
		printf("0\n");
		return 0; 
	}
	
	printf("%d",cal(0,strlen(str)-1));	
}