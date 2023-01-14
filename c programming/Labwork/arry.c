#include<stdio.h>

void main()
{
	int arr1[3],arr2[3];
	int i;
	
	printf("Enter Arry 1.---->\n\n");
	for(i=0;i<3;i++)
	{
    	printf("Enter the Number [%d] : ",i);
    	scanf("%d",&arr1[i]);
    }
    
    printf("\nEnter Arry 2.---->\n\n");
    for(i=0;i<3;i++)
    {
    	printf("Enter the Number [%d] : ",i);
    	scanf("%d",&arr2[i]);
	}
	
	printf("\nArry 1.---->\n\n");
    for(i=0;i<3;i++)
    {
    	printf("Your Number is [%d] : %d\n",i,arr1[i]);
	}
	
	printf("\nArry 2.---->\n\n");
	for(i=0;i<3;i++)
	{
		printf("Your Number is [%d] : %d\n",i,arr2[i]);
	}
	
	printf("Addition of Arr1. And Arr2.------>\n\n");
    for(i=0;i<3;i++)
    {
    	printf("Addition [%d] : %d\n",i,(arr1[i]+arr2[i]));
	}
    
    
    
    
    
}