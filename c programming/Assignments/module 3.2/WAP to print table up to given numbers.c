#include<stdio.h>

void main()
{
	int i,n,a,b;
	printf("Enter the start number : ");
	scanf("%d",&a);
	printf("Enter the end number : ");
	scanf("%d",&b);
	
	for(i=a;i<=b;i++)
	{
		for(n=1;n<=10;n++)
		{
			printf("%d x %d = %d\n",i,n,(i*n));
		}
	}
}