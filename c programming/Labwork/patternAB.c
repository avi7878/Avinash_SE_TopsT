#include<stdio.h>

void main()
{
	char i,j,charr,count='A';
	
	printf("Enter the charcter : ");
	scanf("%c",&charr);
	
	for(i='A';i<=charr;i++)
	{
		for(j='A';j<=i;j++)
		{
			printf("%c",j);
			
		}
		printf("\n");
	}
}