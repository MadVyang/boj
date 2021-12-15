#include <stdio.h>

int myz[100];
int myo[100];

int z(int n)
{
	if(myz[n]) return myz[n];
	
	if(n==0) return 1;
	if(n==1) return 0;
	myz[n]=z(n-1)+z(n-2);
	return myz[n];
}
int o(int n)
{
	if(myo[n]) return myo[n];
	
	if(n==0) return 0;
	if(n==1) return 1;
	myo[n]=o(n-1)+o(n-2);
	return myo[n];
}

int main()
{
	int N;
	scanf("%d",&N);
	
	int i,tmp;
	for(i=0;i<N;i++)
	{
		scanf("%d",&tmp);
		printf("%d %d\n",z(tmp),o(tmp));
	}
}