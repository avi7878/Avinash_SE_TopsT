           // WAP find simple interest...

#include<stdio.h>

void main()
{
	int principal,rate,time,interest;
	
	printf("Enter the principal : ");
	scanf("%d",&principal);

    printf("Enter the rate : ");
    scanf("%d",&rate);
    
    printf("Enter the time : ");
    scanf("%d",&time);
    
    interest = principal * rate * time /100;
    printf("The simple interest is %d",interest);

}