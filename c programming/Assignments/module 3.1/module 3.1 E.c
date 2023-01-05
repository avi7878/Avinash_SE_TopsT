   //  WAP to check if the given year is a leap year or not.
   
#include<stdio.h>

void main()
{
	int y;
	printf("Enter any year : ");
	scanf("%d",&y);
	
	if(y%4==0)
	{
		printf("year is leapyear");
	}
    else 
    { 
        printf("year is not leapyear");
	}
}