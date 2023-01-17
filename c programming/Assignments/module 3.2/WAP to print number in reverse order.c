                  // WAP to print number in reverse order e.g.: number = 64728 ---> reverse = 82746.
                  
#include<stdio.h>

void main()

{
	int num,r;
	
	printf("Enter the Number : ");
	scanf("%d",&num);
	
	while(num>0)
	{
		r=num%10;
		printf("%d",r);
		num=num/10;
	}
}