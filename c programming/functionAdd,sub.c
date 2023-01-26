#include<stdio.h>

void add()
{

	int a,b,choice;
	
	printf("Enter the Number : ");
	scanf("%d",&a);
	printf("Enter the Number : ");
	scanf("%d",&b);
	printf("A = %d, B = %d\n",a,b);

	printf("\nPress1. to Addition.");
	printf("\nPress2. to Subtrect.");
	printf("\nPress3. to Multiply");
	printf("\nPress4. to Divison.");
	printf("\n\nEnter your choice? : ");
	scanf("%d",&choice);
	
	switch(choice)
	{
		case 1 :printf("\nAddition is : %d",(a+b));
		break;
		case 2 :printf("\nSubtrect is : %d",(a-b));
		break;
		case 3 :printf("\nMultiply is : %d",(a*b));
		break;
		case 4 :printf("\nDivison is : %.2f",((float)a/b));
		break;
	}
	
	
	
}

void main()
{
	add();
}
