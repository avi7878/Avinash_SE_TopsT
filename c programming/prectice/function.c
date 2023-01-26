#include<stdio.h>

void f1()
{
	printf("\nFunction1 called.");
}

void f2()
{
	printf("\nFunction2 called.");
}

void main()
{
	printf("\nStart Function.");
	f1();
	f2();
	printf("\nEnd Function.");
}