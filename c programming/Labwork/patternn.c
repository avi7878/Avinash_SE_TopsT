#include<stdio.h>

void main()
{
	int i,j,no,count=1;
	
	printf("Enter the Number : ");
	scanf("%d",&no);
	
	for(i=1;i<=no;i++)
	{
		for(j=1;j<=i;j++)
		{
			printf("%d",j);
		}
		printf("\n");
	}
}