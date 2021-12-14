#include <stdio.h>
#include <string.h>
int main()
{
	int i;
	char str[200];
	int arr[30];
	for(i=0;i<26;i++)
	{
		arr[i]=-1;
	}
	scanf("%s",&str);
	for(i=0;i<strlen(str);i++)
	{
		if(arr[str[i]-'a']==-1) arr[str[i]-'a']=i;
	}
	
	for(i=0;i<26;i++)
	{
		printf("%d ",arr[i]);
	}
}