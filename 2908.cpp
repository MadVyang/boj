#include <stdio.h>

int rev(int n)
{
	int R=0;
	
	while(n)
	{
		R*=10;
		R+=n%10;
		n/=10;
	}
	return R;
}

int main()
{
	int a,b;
	scanf("%d%d",&a,&b);
	printf("%d",rev(a)>rev(b)?rev(a):rev(b));
	return 0;
}