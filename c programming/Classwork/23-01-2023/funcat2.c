#include<stdio.h>

void add(int x,int y)
{
	printf("\nInside UDF X = %d, Y = %d",x,y);
	printf("\nAddition : %d",(x+y));
}

void main()
{
	int a,b;
	
	printf("Enter the value of A : ");
	scanf("%d",&a);
	printf("Enter the value of B : ");
	scanf("%d",&b);
	
	printf("\nInside Main A = %d, B = %d",a,b);
	printf("\nStart function");
	add(a,b);
	printf("\nStop function");
}