#include<stdio.h>

void main()
{
	int num1,num2,addition,subtraction,multiplication,division,modulo;
	
	printf("Enter a first number: ");
	scanf("%d",&num1);
    printf("Enter a second number: ");
    scanf("%d",&num2);
    
    addition = num1 + num2 ;
	subtraction = num1 - num2 ;
	multiplication = num1 * num2 ;
	division = num1 / num2	;
	
	printf("The result of addition is : %d\n",addition);
    printf("The result of subtraction is : %d\n",subtraction);
	printf("The result of multiplication : %d\n",multiplication);
	printf("The result of division : %d\n",division);
		
	
}