#include<stdio.h>

void main()
{
	int a,b,c;
	printf("\nEnter the A, B, C, : ");
	scanf("%d%d%d",&a,&b,&c);
/*	printf("\nEnter the  B = ");
	scanf("%d",&b);
	printf("\nEnter the C = ");
	scanf("%d",&c);
*/	
	printf("\nA = %d,B = %d,C = %d",a,b,c);
	
	if(a>b)
	{
		if(a>c)
		{
			printf("\nA is Greater.");
		}
		else
		{
			printf("\nC is Greater.");
		}
	}
	else
	{
		if(b>c)
		{
			printf("\nB is Greater.");
		}
		else
		{
			printf("\nC is Greater.");
		}
	}
	
	
	
}