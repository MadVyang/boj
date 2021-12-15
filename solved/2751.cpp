#include <stdio.h>
#include <algorithm>


int N;
int arr[1000001];
int main()
{
	using namespace std;
	
	scanf("%d",&N);
	int i;
	int tmp;
	for(i=0;i<N;i++)
	{
		scanf("%d",&arr[i]);
	}
	
	stable_sort(arr,arr+N);
	
	for(i=0;i<N;i++) printf("%d\n",arr[i]);
}