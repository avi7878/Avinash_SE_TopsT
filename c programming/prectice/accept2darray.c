#include<stdio.h>

void main()
{
	int i,j,matrix1[3][3],matrix2[3][3];
	
	printf("\n\n\t\t\xB2\xB2\xB2\xB2\xB2\xB2\xB2 Enter Matrix1 \xB2\xB2\xB2\xB2\xB2\xB2\xB2\n\n");
	for(i=0;i<3;i++)
	{
		for(j=0;j<3;j++)
		{
			printf("\t\tEnter the Element1[%d][%d] : ",i,j);
			scanf("%d",&matrix1[i][j]);
		}
	}
	
	
	printf("\n\n\t\t\xB2\xB2\xB2\xB2\xB2 Enter Matrix2 \xB2\xB2\xB2\xB2\xB2");
	for(i=0;j<3;i++)
	{
		for(j=0;j<3;j++)
		{
			printf("\t\tEnter the Element2[%d][%d] : ",i,j);
			scanf("%d",&matrix2[i][j]);
		}
	}
	
	
	printf("\n\n\t\t\xB2\xB2\xB2\xB2\xB2 Matrix1 \xB2\xB2\xB2\xB2\xB2\n\n");
	for(i=0;i<3;i++)
	{
		for(j=0;j<3;j++)
		{
			printf("\t\t%d",matrix1[i][j]);
		}
		printf("\n");
	}
}