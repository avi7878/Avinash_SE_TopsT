                      //WAP to print number in reverse order e.g.: number = 64728 ---> reverse = 82746.
#include<stdio.h>

void main()
{
	int num,i,n;
	
	printf("Enter the Number : ");
	scanf("%d",&num);
	
	while(num>0)
	{
		n=num%10;
	    printf("%d",n);
	    num=num/10;
	}
	
}