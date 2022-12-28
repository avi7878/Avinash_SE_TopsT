#include<stdio.h>

void main()
{
	int age;
	printf("\nEnter your age : ");
	scanf("%d",&age);
	
	if(age>=18)
    {
    	printf("\nYou are eligible to vote.");

	}
    else
    {
    	printf("\nYou are not eligible to vote.");
	}


}