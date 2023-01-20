#include<stdio.h>

void main()
{
	int i,j,k,no;
	printf("Enter the Number : ");
	scanf("%d",&no);
	
	for(i=1;i<=no;i++)
	{
		for(j=no;j>=i;j--)
		{
			printf(" ");
		}
		for(k=1;k<=i;k++)
		{
			printf("* ");
		}
		printf("\n");
	}
}