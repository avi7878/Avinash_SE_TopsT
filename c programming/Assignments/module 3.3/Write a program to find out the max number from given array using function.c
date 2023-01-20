#include<stdio.h>

void main()
{
	int arr[5],max,min,remainder;
	int i;
	
	for(i=0;i<5;i++)
	{
        printf("Enter the Number[%d] : ",i);
    	scanf("%d",&arr[i]);
    }
	max=arr[0];
	
	for(i=0;i<5;i++)
	{
		if(arr[i]>max)
		{
			max=arr[i];
	    }
	}
	min=arr[0];
	for(i=0;i<5;i++)
	{
		if(arr[i]<min)
		{
			min=arr[i];
		}
	}
	printf("max number is : %d\n",max);
	printf("Minimum number is : %d",min);
}
