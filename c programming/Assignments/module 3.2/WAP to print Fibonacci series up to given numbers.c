#include<stdio.h>

void main()
{
	int i,f=0,s=1,number,num;
	
	printf("Enter the nuumber : ");
	scanf("%d",&num);
	printf("\nYour fibonacci Number.---->\n");
	for(i=2;i<=num;i++)
	{
		number=f+s;
		printf("%d\n",number);
		f=s;
		s=number;
    }
}