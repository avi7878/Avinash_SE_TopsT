#include<stdio.h>

void add(int i,int j)
{
	printf("\nInside UDF i = %d j = %d",i,j);
	printf("\nAddition : %d",(i+j));
}

void main()
{
	int a,b;
	
	printf("Enter the A : ");
	scanf("%d",&a);
	printf("Enter the B : ");
	scanf("%d",&b);
	printf("Main A = %d B = %d",a,b);
	printf("\nStart function.");
	add(a,b);
	printf("\nStop function.");
	
}