#include <stdio.h>

int main()
{	
	int x,y;
	scanf("%d%d",&x,&y);
	
	int num=y-1;
	
	while(x>1)
	{
		if(x==3) num+=28;
		else if(x==5 || x==7 || x==10 || x==12) num+=30;
		else num+=31;
		x--;
	}
	
	if(num%7==0) printf("MON");
	else if(num%7==1) printf("TUE");
	else if(num%7==2) printf("WED");
	else if(num%7==3) printf("THU");
	else if(num%7==4) printf("FRI");
	else if(num%7==5) printf("SAT");
	else if(num%7==6) printf("SUN");
}