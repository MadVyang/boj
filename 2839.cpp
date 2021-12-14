#include <stdio.h>

int arr[5005];
int N;

int min(int a, int b)
{
	return a>b?b:a;
}

int my(int n)
{
	if(arr[n]) return arr[n];
	if(n==4 || n <3) return 999999999;
	else if(n==3 || n==5) return 1;
	else arr[n] = min(my(n-3), my(n-5))+1;
	return arr[n];
}
int main()
{
	scanf("%d",&N);
	int ans = my(N);
	if(ans>=999999999) printf ("-1");
	else printf("%d", my(N));
}	