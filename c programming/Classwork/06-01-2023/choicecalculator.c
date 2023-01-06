#include<stdio.h>

void main()
{
	int a,b,choice;
	printf("\n\n\t\t\xB2\xB2\xB2\xB2\xB2 Choice Calculator \xB2\xB2\xB2\xB2\xB2");
	printf("\n\n\t\tEnter A : ");
	scanf("%d",&a);
	printf("\n\n\t\tEnter B : ");
	scanf("%d",&b);
	printf("\n\n\t\tA = %d, B = %d",a,b);
	printf("\n\t\t===================================");
	printf("\n\n\t\tpress 1. for Addition");
	printf("\n\n\t\tpress 2. for Subtraction");
	printf("\n\n\t\tpress 3. for Multiplication");
	printf("\n\n\t\tpress 4. for Division");
	printf("\n\t\t===================================");
	printf("\n\t\tEnter your choice ? ");
	scanf("%d",&choice);
	
	if(choice==1)
	{
		printf("\n\n\tAddition : %d",(a+b));
	}
	else if(choice==2)
	{
		printf("\n\n\tSubtraction : %d",(a-b));
	}
	else if(choice==3)
	{
		printf("\n\n\tMultiplication : %d",(a*b));
	}
	else if(choice==4)
    {
    	printf("\n\n\tDivision : %.2f",((float)a/b));
	}
	else
	{
		printf("\n\nInvalide choice");
	}
}