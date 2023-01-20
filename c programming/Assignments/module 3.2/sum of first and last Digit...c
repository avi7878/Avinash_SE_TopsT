#include<stdio.h>

void main()

{
	int no,firstdigit,lastdigit,sum;
	
	printf("Enter the Number : ");
    scanf("%d",&no);
	
	lastdigit = no%10;
	
	while(no>10)
	{
	   no = no / 10;	
	}
	
	firstdigit = no;
	
	sum = firstdigit + lastdigit;
	
	printf("Sum of first and last Digit : %d",sum);
		
}