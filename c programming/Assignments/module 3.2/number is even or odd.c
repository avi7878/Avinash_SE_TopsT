#include<stdio.h>

void main()
{
	int n;
	printf("Enter the number : ");
	scanf("%d",&n);
	
	(n%2==0)? (printf("number is odd")): (printf("number is even"));
}