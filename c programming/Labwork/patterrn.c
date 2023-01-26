#include<stdio.h>

void main()
{
	int i,j,no,k;
	
	printf("Enter the number : ");
	scanf("%d",&no);
	
	for(k=no;k<=0;k--)
	{
		printf(" ");
		for(i=0;i<no;i++)
		{
			for(j=0;j<i;j++)
			{
				printf("*");
			}
		}
	}
}