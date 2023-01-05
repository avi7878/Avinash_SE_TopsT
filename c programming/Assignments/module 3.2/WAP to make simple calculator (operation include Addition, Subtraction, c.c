#include<stdio.h>

void main()
{
	int a,b,addition,subtraction,division,multiplication;
	printf("Enter the A : ");
    scanf("%d",&a);   
    printf("\nEnter the B : ");
    scanf("%d",&b);
    printf("A = %d, B = %d",a,b); 
    addition = a + b;
    subtraction = a - b;
    division = a / b;
    multiplication = a * b;
    printf("\naddition = %d",addition);
    printf("\nsubtraction = %d",subtraction);
    printf("\ndivision = %d",division);
    printf("\nmultiplication = %d",multiplication);
}
