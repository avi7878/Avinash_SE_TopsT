#include<stdio.h>

void add()
{
	int d,f;
	printf("a = %d b = %d",d,f);
	printf("\nAddition is : %d",(d+f));
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
