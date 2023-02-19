#include<stdio.h>

void main()
{
	int matrix1[3][3],matrix2[3][3];
	int i,j;
	
	printf("Enter Matrix1\n");
	
	for(i=0;i<3;i++)
	{
		for(i=0;j<3;j++)
		{
			printf("Matrix1[%d][%d] : ",i,j);
			scanf("%d",&matrix1[i][j]);
		}
	}
}