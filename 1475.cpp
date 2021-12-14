#include <stdio.h>

int arr[10];
int N;
int main(){
	scanf("%d",&N);
	
	if(N==0) arr[0]=1;
	while(N){
		arr[N%10]++;
		N/=10;
	}
	
	int tmp=arr[6]+arr[9];
	arr[6]=tmp/2;
	arr[9]=tmp-arr[6];
	
	int i;
	int max=-1;
	for(i=0;i<10;i++){
		if(arr[i]>max) max=arr[i];
	}
	printf("%d",max);
}