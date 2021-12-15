#include <stdio.h>

int N;
int arr[105];
int main()
{
	int a,b,c;
	scanf("%d%d%d",&a,&b,&c);
	arr[a]++;
	arr[b]++;
	arr[c]++;
	
	int i;
	int chk=0;
	for(i=0;i<105;i++)
	{
		if(arr[i]) chk+=arr[i];
		if(chk>=2)
		{
			printf("%d",i);
			return 0;
		}
	}
}