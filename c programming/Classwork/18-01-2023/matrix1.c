#include<stdio.h>

void main()
{
	int matrix1[3][3];
	int i,j;
	
	printf("\n\t\t\t\t\xB2\xB2\xB2\xB2\xB2\xB2\xB2 Enter the matrix1 \xB2\xB2\xB2\xB2\xB2\xB2\xB2\n\n");
	for(i=0;i<3;i++)
	{
		for(j=0;j<3;j++)
		{
			printf("\t\t\t\tEnter the Element[%d][%d] : ",i,j);
			scanf("%d",&
			matrix1[i][j]);
		}
		printf("\n");
	}
	
	printf("\t\t\t\t\t\t\t\n\n\xB2\xB2\xB2\xB2\xB2\xB2\xB2 Matrix1 \xB2\xB2\xB2\xB2\xB2\xB2\xB2\n\n");
	for(i=0;i<3;i++)
	{
		for(j=0;j<3;j++)
		{
			printf("\t\t%d",matrix1[i][j]);
		}
		printf("\n");
	}
}