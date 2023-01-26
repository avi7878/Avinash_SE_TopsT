// WAP to find factorial using recursion.
#include<stdio.h>

int fact(int n)
{
	if(n==0)
	return(1);
	else
	return(n*fact(n-1));
}

void main()
{
	int n,f;
	printf("Enter factorial No : ");
	scanf("%d",&n);
	f=fact(n);
	printf("Factorial is %d",f);
	getch();
	
}