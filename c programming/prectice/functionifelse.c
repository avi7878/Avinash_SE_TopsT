#include<stdio.h>

void a1();
{
	int a=5,b=6;
	
	if(a>b)
	{
		printf("%d is greater.",a);
	}
	else
	{
		printf("%d is greater.",b);
	}
}


void main()
{
	printf("Condition1.");
	a1();
	printf("End");
}