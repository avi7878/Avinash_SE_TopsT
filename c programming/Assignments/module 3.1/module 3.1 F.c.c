#include<stdio.h>

void main()
{
	int days,years;years,days;
	printf("Enter the number of days : ");
	scanf("%d",&days);
	years=days/365;
	printf("\nmumber of years is : %d",years);
	
	printf("\n\nEnter the number of years : ");
	scanf("%d",&years);
	days=years*365;
	printf("\nnumber of days is : %d",days);
}