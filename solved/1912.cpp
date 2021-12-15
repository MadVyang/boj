#include <stdio.h>
int N;
int arr[100001];
long long sol[100001];
int main(){
	scanf("%d",&N);
	for(int i=0;i<N;i++){
		scanf("%d",&arr[i]);
		if(i>0) {
			sol[i]=(arr[i]>(arr[i]+sol[i-1]))?arr[i]:(arr[i]+sol[i-1]);
		} else {
	        sol[0]=arr[0];
        }
	}
	long long max=arr[0];
	for(int i=0;i<N;i++){
		if(sol[i]>max) max=sol[i];
	}
	printf("%lld",max);
}