#include<stdio.h>

int add(int d,int g)
{
	printf("\nInside UDF A = %d, B = %d",d,g);
	return d+g;
}

void main()
{
	int a,b,sum;
	
	printf("Enter the A : ");
	scanf("%d",&a);
	printf("Enter the B : ");
	scanf("%d",&b);
	
	sum = add(a,b);
	printf("\nAddtion : %d",sum);
	if(sum%2==0)
	{
		printf("\nSum in Even.");
	}
	else
	{
		printf("\nSum os Odd.");
	}
	
	
}