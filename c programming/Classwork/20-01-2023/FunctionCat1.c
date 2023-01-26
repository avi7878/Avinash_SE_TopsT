#include<stdio.h>

void f1()
{
	f2();
	printf("\nFunction1 called.");
}

void f2()
{
	printf("\nFunction2 called.");
}

void main()
{
	printf("\nBefore Function called.");
	f1();
	f2();
	printf("\nAfter Function called.");
}

