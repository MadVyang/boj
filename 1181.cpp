#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <algorithm>

int N;
char list[20005][55];
char tmp[55];

int comp(const void *a,const void *b)//(char a[],char b[])
{
	int i;
	if(strlen((char *)a)>strlen((char *)b)) return 1;
	else if(strlen((char *)a)<strlen((char *)b)) return 0;
	else
	{
		for(i=0;i<strlen((char *)a);i++)
		{
			if(((char *)a)[i]>((char *)b)[i]) return 1;
			else if(((char *)a)[i]<((char *)b)[i]) return 0;
		}
		
		return 0;
	}
}

int main()
{
	scanf("%d",&N);
	int i,j;
	for(i=0;i<N;i++)
	{
		scanf("%s",&list[i]);
	}
	/*
	int chk;
	for(i=N-1;i>0;i--)
	{
		for(j=0;j<i;j++)
		{
			chk=comp(list[j],list[j+1]);
			if(chk)
			{
				strcpy(tmp,list[j]);
				strcpy(list[j],list[j+1]);
				strcpy(list[j+1],tmp);
			}
		}
	}*/
	qsort(list,N,sizeof(list[0]),comp);
	
	for(i=0;i<N;i++)
	{
		if(i>0 && strcmp(list[i],list[i-1])==0) continue;
		printf("%s\n",&list[i]);
	}
}