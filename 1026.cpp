#include <stdio.h>
#include <algorithm>

int A[60],B[60];

int main()
{
	int N;
	scanf("%d",&N);
	
	int i;
	for(i=0;i<N;i++)
	{
		scanf("%d",&A[i]);
	}
	for(i=0;i<N;i++)
	{
		scanf("%d",&B[i]);
	}
	
	std::sort(A,A+N);
	std::sort(B,B+N);
	
	int S=0;
	for(i=0;i<N;i++)
	{
		S+=A[i]*B[N-i-1];
	}
	printf("%d",S);
}