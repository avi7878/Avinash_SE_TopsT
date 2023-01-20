#include<stdio.h>

void main()
{
	int arr[5],max,min;
	int i;
	
	for(i=0;i<5;i++)
	{
		printf("Enter the number[%d] : ",i);
		scanf("%d",&arr[i]);
		
	}
	max=arr[0];
	
	for(i=0;i<5;i++)
	{
	    if(max<arr[i])
		{
		   max=arr[i];	
		}	
	}
	min=arr[0];
	for(i=0;i<5;i++)
	{
	    if(min>arr[i])
		{
			min=arr[i];
		}	
	}
	printf("max number is : %d\n",max);
	printf("Minimum number is : %d",min);
	
}