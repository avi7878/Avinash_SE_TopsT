#include<stdio.h>

void main()
{
	int i,j,no,count=1;
	
	printf("Enter the Number : ");
	scanf("%d",&no);
	
	for(i=0;i<no;i++)
	{
		for(j=0;j<i;j++)
		{
			printf("%d",count);
			++count;
		}
		printf("\n");
	}
}