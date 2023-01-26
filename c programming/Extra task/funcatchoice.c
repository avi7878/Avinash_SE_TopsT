#include<stdio.h>

int add(int i,int j)
{
	printf("\nInside UDF A = %d B = %d",i,j);
	return i+j;
}
int sub(int k,int l)
{
	printf("\nInside UDF A = %d B = %d",k,l);
	return k-l;
}
int mul(int d,int e)
{
	printf("\nInside UDF A = %d B = %d",d,e);
	return d*e;
}
int div(int f,int g)
{
	printf("\nInside UDF A = %d B = %d",f,g);
	return f/g;
}


void main()
{
	int a,b,sum,choice;
	
	printf("Enter the number : ");
	scanf("%d",&a);
	printf("Enter the number : ");
	scanf("%d",&b);
	printf("A = %d B = %d",a,b);
	printf("\nStart function.");
	sum=add(a,b);
	printf("\nPress 1. to Addition.");
	sum=sub(a,b);
	printf("\nPress 2. to Subtrect.");
	sum=mul(a,b);
	printf("\nPress 3. to Multiply.");
	sum=div(a,b);
	printf("\nPress 4. to Division.");
	printf("\nEnter your choice? : ");
	scanf("%d",&choice);
	
	switch(choice)
	{
		case 1: printf("Addition is : %d",sum);
		break;
		case 2: printf("Subtrection is : %d",sum);
		break;
		case 3: printf("Multiply is : %d",sum);
		break;
		case 4: printf("Division is : %.2f",(float)sum);
		break;
		default: printf("Invalid Number.");
	}	
}