#include<stdio.h>

void add()
{
	int a,b;
	printf("\nAddition is : %d",(a+b));
}

void main()
{
	int a,b;
	
	printf("Enter the Number : ");
	scanf("%d",&a);
	printf("Enter the Number : ");
	scanf("%d",&b);
	
	printf("A = %d, B = %d",a,b);
	add();
}
