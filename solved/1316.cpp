#include <stdio.h>
#include <string.h>

int arr[30];
int main()
{
	int N;
	scanf("%d",&N);
	int i,len;
	char s[105];
	int cnt=0;
	while(N--)
	{
		for(i=0;i<30;i++)
		{
			arr[i]=0;
		}
		cnt++;
		scanf("%s",&s);
		len=strlen(s);
		for(i=0;i<len;i++)
		{
			if(arr[s[i]-'a']==1)
			{
				//printf("%d %d\n",N,i);
				cnt--;
				break;
			}
			arr[s[i]-'a']=1;
			if(s[i]==s[i+1])
			{
				while(s[i]==s[i+1])
				{
					i++;
				}
			}
		}
	}
	printf("%d",cnt);
}