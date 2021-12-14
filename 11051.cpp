#include <stdio.h>

int m[1005][1005];

int f(int n,int k)
{
	if(k==0) return 1;
	if(k==1) return n;
	if(k==n-1) return n;
	if(k==n) return 1;
	
	if(m[n][k]) return m[n][k];
	
	m[n][k]=f(n-1,k-1)+f(n-1,k);
	m[n][k]%=10007;
	return m[n][k];
}

int main()
{
	int n,k;
	scanf("%d%d",&n,&k);
	
	printf("%d",f(n,k));
}