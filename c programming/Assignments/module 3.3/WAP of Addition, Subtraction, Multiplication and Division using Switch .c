#include<stdio.h>

void main()
{
	int a,b,choice;
	
	printf("Enter A : ");
	scanf("%d",&a);
	printf("Enter B : ");
	scanf("%d",&b);
	
	printf("A = %d, B = %d\n",a,b);
	
	printf("\npress1. Addition\npress2. Subtrect\npress3. Multiply\npress4. Division\n");
	printf("\nEnter your choice : ");
	scanf("%d",&choice);
	switch(choice)
	{
		case 1 : printf("\nAddition : %d",(a+b));
		         break;
		case 2 : printf("\nSubtrect : %d",(a-b));
		         break;
		case 3 : printf("\nMultiply : %d",(a*b));
		         break;
		case 4 : printf("\nDivision : %d",(a/b));
		         break;
		default : printf("\nInvalid choice");
		         break;        
	}
}