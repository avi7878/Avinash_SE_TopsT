#include<stdio.h>

int add(int d,int c)
{
	printf("\nInside UDF is D = %d C = %d",d,c);
	
	return d+c;	
}

void main()
{
	int a,b,sum;
	
	printf("Enter the Number : ");
	scanf("%d%d",&a,&b);
	printf("A = %d B = %d",a,b);
	printf("\n\nFunction Start.");
	sum = add(a,b);
	printf("\n\nAddition is : %d",sum);
	if(sum%2==0)
	{
		printf("\nSum is even.");
	}
	else
	{
		printf("\nSum is odd.");
	}
}