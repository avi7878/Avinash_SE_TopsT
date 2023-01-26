#include<stdio.h>

void f1()
{
	int a,b;
	printf("\nEnter the Number1 : ");
	scanf("%d",&a);
	printf("Enter the Number2 : ");
	scanf("%d",&b);
	
	if(a>b)
	{
		printf("%d is Greater.",a);
	}
	else
	{
		printf("%d is Greater.",b);
	}
	printf("\n");
}

void main()
{
	printf("\nWho is Greater?\n");
	f1();
	f1();
	printf("\nEnd Function.");
}
