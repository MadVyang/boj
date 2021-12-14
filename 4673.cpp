#include <stdio.h>

int arr[10005];
void my(int n)
{
	if(n>10003) return;
	if(arr[n]) return;
	
	int next=n;
	while(n)
	{
		next+=n%10;
		n/=10;
	}
	my(next);
	arr[next]=1;
}

int main()
{
	int i;
	for(i=1;i<=10000;i++)
	{
		my(i);
	}
	
	for(i=1;i<=10000;i++)
	{
		if(arr[i]==0) printf("%d\n",i);
	}
}