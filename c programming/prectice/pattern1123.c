#include<stdio.h>

void main()
{
	char i,j,no,count=1;
	
	printf("Enter the number : ");
	scanf("%c",&no);
	
	for(i=1;i<no;i++)
	{
		for(j=1;j<=i;j++)
		{
			printf("%c",count);
			count++;
		}
		printf("\n");
		
	}
}