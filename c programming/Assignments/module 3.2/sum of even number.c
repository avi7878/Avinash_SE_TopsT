                    // Sum of even numbers
#include<stdio.h>

void main()
{
	int a,i,n;
	printf("Enter the number : ");
	scanf("%d",&i);
	printf("Enter the end number : ");
	scanf("%d",&n);
	
	for(a=i;i<=n;i+=2)
	{
		printf("The even Number is : %d\n",i);
	}
}