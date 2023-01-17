#include<stdio.h>

void main()
{
	int i,arr1[2],arr2[2];
	
	printf("Enter your value Array1.---->\n\n");
	for(i=0;i<2;i++)
	{
		printf("Enter your value [%d] : ",i);
		scanf("%d",&arr1[i]);
	}
	
	printf("\nEnter your value Array2.---->\n\n");
	for(i=0;i<2;i++)
	{
		printf("Enter your value [%d] : ",i);
		scanf("%d",&arr2[i]);
	}
	
	printf("\nArray1.---->\n\n");
	for(i=0;i<2;i++)
	{
		printf("Your value is [%d] : %d\n",i,arr1[i]);
	}
	
	printf("\nArray2.---->\n\n");
	for(i=0;i<2;i++)
	{
	    printf("Your value is [%d] : %d\n",i,arr2[i]);	
	}
	
	printf("\nSubtraction of Array1 and Array2.---->\n\n");
	for(i=0;i<2;i++)
	{
	    printf("Subtraction [%d] : %d\n",i,(arr1[i]-arr2[i]));	
	}	
	
	
	
}