#include<stdio.h>

void main()
{
	int matrix1[3][3],matrix2[3][3];
	int i,j;
	
	printf("==========Matrix1===========\n");
	for(i=0;i<3;i++)
	{
		for(j=0;j<3;j++)
		{
			printf("Enter the Element[%d][%d] : ",i,j);
			scanf("%d",&matrix1[i][j]);
		}
		printf("\n");
	}
	
	for(i=0;i<3;i++)
	{
		for(j=0;j<3;j++)
		{
			printf("%d\t",matrix1[i][j]);
		}
		printf("\n");
	}
	
	printf("===========Matrix2============\n");
	for(i=0;i<3;i++)
	{
		for(j=0;j<3;j++)
		{
			printf("Enter the Element[%d][%d] : ",i,j);
			scanf("%d",&matrix2[i][j]);
		}
		printf("\n");
	}
	
	for(i=0;i<3;i++)
	{
		for(j=0;j<3;j++)
		{
			printf("%d\t",matrix2[i][j]);
		}
		printf("\n");
	}
	printf("====Addition of matrix\n====");
	for(i=0;i<3;i++)
	{
		for(j=0;j<3;j++)
		{
			printf("%d\t",(matrix1[i][j]+matrix2[i][j]));
		}
		printf("\n");
	}
	
	
	
	
	
	
	
	
	
	
	
	
}