            //Write a program to find out the max from given number (E.g., No: -1562 Max number is 6).
#include<stdio.h>

void main()
{
	int no,max,remainder;
	printf("Enter the Number : ");
	scanf("%d",&no);
	
	while(no>0)
	{
		remainder=no%10;
		if(max<remainder)
		{
		max=remainder;
	    }
	    no=no/10;
	}
	printf("max number is : %d",max);
}
