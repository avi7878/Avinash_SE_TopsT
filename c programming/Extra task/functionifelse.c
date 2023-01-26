#include<stdio.h>

int add(int i,int j)
{
	printf("\nA = %d,B = %d",i,j);
	return i+j;
}
    




void main()
{
	int a,b;
	
	printf("Enter the A : ");
	scanf("%d",&a);
	printf("Enter the B : ");
	scanf("%d",&b);
	
	add(a,b);
}