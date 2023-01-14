#include<stdio.h>

void main()

{
	int arr1[5];
	int i;
	
	for(i=0;i<5;i++)
	{
		printf("Enter Element[%d] : ",i);
		scanf("%d",&arr1[i]);
	}
	
	for(i=0;i<5;i++)
	{
		printf("%d\t",arr1[i]);
	}
	
}