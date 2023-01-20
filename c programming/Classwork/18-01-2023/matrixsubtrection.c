#include<stdio.h>

void main()
{
	int matrix1[3][3],matrix2[3][3];
	int i,j;
	
	printf("\t\t\tElement of Matrix1\n\n");
	
	for(i=0;i<3;i++)
	{
		for(j=0;j<3;j++)
		{
			printf("\t\tEnter the Element[%d][%d] : ",i,j);
			scanf("%d",&matrix1[i][j]);
		}
		printf("\n");
	}
	
	printf("\t\t\tElement of Matrix2\n\n");
	
	for(i=0;i<3;i++)
	{
		for(j=0;j<3;j++)
		{
			printf("\t\tEnter the Element[%d][%d] : ",i,j);
			scanf("%d",&matrix2[i][j]);
		}
		printf("\n");
	}
	
	printf("\t\t\tDisplay of Matrix1\n\n");
	
	for(i=0;i<3;i++)
	{
		for(j=0;j<3;j++)
		{
			printf("\t\t%d",matrix1[i][j]);
		}
		printf("\n");
	}
	
	printf("\t\t\tDisplay of matrix2\n\n");
	
	for(i=0;i<3;i++)
	{
		for(j=0;j<3;j++)
		{
			printf("\t\t%d",matrix2[i][j]);
		}
		printf("\n");
	}
	
	printf("\t\t\tSubtraction of Matrix\n\n");
	
	for(i=0;i<3;i++)
	{
		for(j=0;j<3;j++)
		{
			printf("\t\t%d",(matrix1[i][j]-matrix2[i][j]));
		}
		printf("\n");
	}
	
}