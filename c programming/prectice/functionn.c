#include<stdio.h>

void ac()
{
	int a,b;
	
	printf("Enter the A and B : ");
	scanf("%d%d",&a,&b);
	
	printf("A = %d B = %d\n",a,b);
	if(a>b)
	{
		printf("%d is greater.\n",a);
	}
	else
	{
		printf("%d is greater.\n",b);
	}
	
	printf("\nAddition of A and B.\n");
	printf("Addition is : %d",(a+b));
}
/*
void add()
{
	int a,b;
	
	printf("Enter the A : ");
	scanf("%d",&a);
	printf("Enter the B : ");
	scanf("%d",&b);
	
	printf("\nAddition is : %d",(a+b));
}*/

void main()
{
	printf("Who is Greater?\n");
	ac();
/*	printf("\nAddition of Two Numbers.\n");
	add();*/
}