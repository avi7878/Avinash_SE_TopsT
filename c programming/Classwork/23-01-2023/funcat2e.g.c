#include<stdio.h>

void swap(int a,int b)
{
	int i;
	
	i = a;
	a = b;
	b = i;
	printf("\nIn swap A = %d, B = %d",a,b);
}

void main()
{
	int a,b; 
	
	printf("Enter the A : ");
	scanf("%d",&a);
	printf("Enter the B : ");
	scanf("%d",&b);
	
	printf("\nIn Main A = %d, B = %d",a,b);
	printf("\nStart function");
	swap(a,b);
	printf("\nEnd function");
}