#include <stdio.h>
#include <string.h>
char str[1000001];
int arr[200];
int main()
{
	//printf("%d %d",'a','A');
	int i;
	scanf("%s",&str);
	int len=strlen(str);
	char c;
	for(i=0;i<len;i++)
	{
		c=str[i];
		if(c>='a') c+='A'-'a';
		arr[c]++;
	}
	
	int max=-1;
	int idx=-1;
	int chk=0;
	for(i=0;i<200;i++)
	{
		if(arr[i]>max)
		{
			idx=i;
			max=arr[i];
			chk=0;
		}
		else if(arr[i]==max)
		{
			chk=1;
		}
	}
	if(chk==1) printf("?");
	else printf("%c",idx);
}