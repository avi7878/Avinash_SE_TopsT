#include<stdio.h>

void main()
{
	int i,j,no;
	
	printf("Enter the Number : ");
	scanf("%d",&no);
	
	for(i=1;j<=no;i++)
    {
    	for(j=1;j<=i;j++)
    	{
    		printf("*");
		}
		printf("\n");
	}


}