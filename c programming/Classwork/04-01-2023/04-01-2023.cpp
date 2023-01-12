#include<stdio.h>

int main()
{
	int a=10;
	int b=20;
	
	printf("\nA = %d, B = %d",a,b);
	
	if(a&&b)
    {
    	printf("\nLine 1 is true");
	}
	else
	{ 
	    printf("\nLine 2 is false");
	}

    b=10,a=10;
    if(a||b)
    {
    	printf("\nLine 3 is true");
	}
    else
    {
    	printf("\nLine 4 is false");
	}
    if(!(a&&b))
    {
    	printf("\nLine 5 is true");
	}
    else
    {
    	printf("\nLine 6 is false");
	}

}