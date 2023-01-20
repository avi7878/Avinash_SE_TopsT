#include<stdio.h>

void main()
{
	int i,j,k;
	
	for(k=5;k<=1;k++)
	{
		printf(" ");
		
	for(i=1;i<=5;i++)
	{
		for(j=1;j<=i;j++)
		{
			printf("*");
		}
		printf("\n");
	}
    }
}