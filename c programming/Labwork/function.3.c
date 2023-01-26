#include<stdio.h>

void swap(int x,int y)
{
	printf("\nInside UDF X = %d Y = %d",x,y);
	
	x=x+y;
	y=x-y;
	x=x-y;
	
	printf("\nSwap Number X = %d Y = %d",x,y);
}


void main()
{
	int a,b;
	
	printf("Enter the Number : ");
	printf("A = %d B = %d",a,b);
	printf("\nSwap a two number.");
	printf("\nStart function.");
	swap(a,b);
	printf("\nStop function.");
}