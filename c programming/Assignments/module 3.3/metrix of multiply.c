#include<stdio.h>

void main()
{
	int matrix1[3],matrix2[3],i,j;
	
	printf("\n\t\t\xB2\xB2\xB2\xB2 Enter the Matrix1. \xB2\xB2\xB2\xB2\n\n");
	
	for(i=0;i<3;i++)
	{
		printf("\t\tEnter Element[%d] : ",i);
		scanf("%d",&matrix1[i]);
	}
	
	printf("\n\t\t\xB2\xB2\xB2\xB2 Enter the Matrix2. \xB2\xB2\xB2\xB2\n\n");
	
	for(i=0;i<3;i++)
	{
		printf("\t\tEnter Element[%d] : ",i);
		scanf("%d",&matrix2[i]);
	}
	
	printf("\n\t\t\xB2\xB2\xB2\xB2\xB2\xB2\xB2\xB2\xB2 Matrix1. \xB2\xB2\xB2\xB2\xB2\xB2\xB2\xB2\xB2\n\n");
	for(i=0;i<3;i++)
	{
		printf("\t\tElement at Index[%d] : %d\n",i,matrix1[i]);
	}
	

	printf("\n\t\t\xB2\xB2\xB2\xB2\xB2\xB2\xB2\xB2\xB2 Matrix2. \xB2\xB2\xB2\xB2\xB2\xB2\xB2\xB2\xB2\n\n");
	
	for(i=0;i<3;i++)
	{
		printf("\t\tElement at Index[%d] : %d\n",i,matrix2[i]);
	}
	
	printf("\n\t\t\xB2\xB2\xB2\xB2 Multipliction of two Matrix. \xB2\xB2\xB2\xB2\n\n");
	
	for(i=0;i<3;i++)
	{
		printf("\t\tMultiply is[%d] : %d\n",i,(matrix1[i]*matrix2[i]));
	}
	
	
	
}