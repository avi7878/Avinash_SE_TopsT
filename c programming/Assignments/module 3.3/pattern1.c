#include<stdio.h>

void main()
{
	char i,j,charr,count='A';
	
	printf("Enter the Charcter : ");
	scanf("%c",&charr);
	
	for(i='A';i<=charr;i++)
	{
		for(j='A';j<=i;j++)
		{
			printf("%c ",count);
			++count;   
		}
		printf("\n");
	}
}