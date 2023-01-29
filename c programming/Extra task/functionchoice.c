#include<stdio.h>

int add(int a,int b)
{
	printf("\nInside UDF I = %d J = %d",a,b);
	return a+b;
}
int sub(int c,int d)
{
	printf("\nInside UDF I = %d J = %d",c,d);
	return c-d;
}
int multi(int e,int f)
{
	printf("\nInside UDF I = %d J = %d",e,f);
	return e*f;
}
int divi(int g,int h)
{
	printf("\nInside UDF I = %d J = %d",g,h);
	return g/h;
}
void main()
{
	int i,j,sum,choice;
	
	printf("Enter the I : ");
	scanf("%d",&i);
	printf("Enter the J : ");
	scanf("%d",&j);
	
	
	printf("I = %d J = %d",i,j);
	printf("\nStart Function.\n");
//	sum=add(i,j);
	printf("\npress 1. to Addition.\n");
	
	printf("\nPress 2. to Subtrect.\n");
//	
	printf("\nPress 3. to Multiplication.\n");
	
	printf("\nPress 4. to Division.\n");
	
	printf("\nEnter your choice? : ");
	scanf("%d",&choice);
	
	switch(choice)
	{
		case 1: 
		sum=add(i,j);
		printf("\nAddition is : %d",sum);
		break;
		case 2: 
		sum = sub(i,j);
		printf("\nSubtrect is : %d",sum);
		break;
		case 3: 
		sum=multi(i,j);
		printf("\nMultiply is : %d",sum);
		return;
		case 4: 
		sum=divi(i,j);
		printf("\nDivision is : %.2f",(float)sum);
		return;
		default : printf("Invalid Number.");
	}
	 
	
}