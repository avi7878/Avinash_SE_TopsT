#include<stdio.h>

void main()
{
	int arry1[3],arry2[3];
	int i;
	
	printf("\nEnter Array 1: \n\n");
	
	for(i=0;i<3;i++)
	{
		printf("Enter Element [%d] : ",i);
		scanf("%d",&arry1[i]);
	}
	
	printf("Enter array 2 : \n\n");
	
	for(i=0;i<3;i++)
	{
		printf("Enter Element [%d] : ",i);
		scanf("%d",&arry2[i]);
	}
     
	 printf("\nArray 1: \n\n");
	 for(i=0;i<=3;i++)
	 {
	 	printf("Element at Index [%d] = %d\n",i,arry1[i]);
	 }	
	
	printf("\nArray 2: \n\n");
	for(i=0;i<3;i++)
	{
		printf("Element at Index [%d] = %d\n",i,arry2[i]);
	}
	
	printf("Addition of Array 1 and Array 2 : \n\n");
	for(i=0;i<3;i++)
	{
		printf("\nAddition[%d] : %d",i,(arry1[i]+arry2[i]));
	}
}