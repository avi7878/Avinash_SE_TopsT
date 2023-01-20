#include<stdio.h>

void main()

{
	int j,i,K,no;
	
	printf("Enter the no : ");
	scanf("%d",&no);
	
	for(K=no;K<=0;K--)
	{
	    for(i=1;i<no;i++)
	    {
	    	for(j=1;j<=i;j++)
	    	{
	    	printf(" * ");
	        }
	        printf("\n");
    	}
    	printf(" ");
    }
}