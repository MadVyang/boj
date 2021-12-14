#include <stdio.h>

int N;
int cnt=0;

int my(int n)
{
	cnt++;
	int a=n/10 + n%10;
	int b=n%10*10 + a%10;
	if(b==N) return cnt;
	return my(b);
}

int main()
{
	scanf("%d",&N);
	printf("%d",my(N));
}