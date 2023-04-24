#include<stdio.h>

void main()
{
	float days,years;
	printf("Enter the number of days : ");
	scanf("%f",&days);
	years=days/365;
	printf("\nnumber of years is : %.2f",(float)years);
	
	printf("\n\nEnter the number of years : ");
	scanf("%f",&years);
	days=years*365;
	printf("\nnumber of days is : %.2f",(float)days);
}