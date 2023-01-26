#include<stdio.h>

void main()
{
	char j,i,count='A',ch;
	
	printf("Enter the value : ");
	scanf("%c",&ch);
	
	for(i='A';i<=ch;i++)
	{
		for(j='A';j<=i;j++)
		{
			printf("%c ",count);
			++count;
		}
		printf("\n");
	}
}