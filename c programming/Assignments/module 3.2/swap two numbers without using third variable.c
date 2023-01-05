#include<stdio.h>

void main()
{
	int a,b;
	printf("Enter first number : ");
	scanf("%d",&a);
	printf("Enter second number : ");
    scanf("%d",&b);
    
    a = a+b;
    b = a-b;
    a = a-b;
    printf("value after swaping");
    printf("\nvalue of a is : %d",a);
    printf("\nvalue of b is : %d",b);
}