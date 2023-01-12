#include<stdio.h>

void main()
{
	int n,n1,i,j;
	printf("Enter the start value : ");
	scanf("%d",&n);
	printf("Enter the end value : ");
	scanf("%d",&n1);
	
	for(i=n;i<=n1;i++)
	{
		for(j=1;j<=10;j++)
		{
			printf("%d x %d = %d\n",i,j,(i*j));
		}
	}
}