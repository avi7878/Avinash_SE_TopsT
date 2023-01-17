#include<stdio.h>

void main()
{
	int i,f=0,s=1,number,num;
	
	printf("Enter the nuumber : ");
	scanf("%d",num);
	
	for(i=2;i<=num;i++)
	{
		number=f+s;
		f=s;
		s=number;
		printf("Your fabonicic number is %d",number);
    }
}