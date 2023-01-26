#include<stdio.h>

void f1()
{
	printf("\nFunction1 called.");
//	f1();
}
void f2()
{
	printf("\nFunction2 called.");
	f2();
}

void main()
{
	printf("\nStart Function.");
	f1();
	f2();
	printf("\nEnd Function.");
}