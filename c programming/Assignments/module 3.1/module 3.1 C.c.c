#include<stdio.h>

void main()
{
	int  r,l,b,h;
	float area;
	  
	printf("Enter radius of circle : ");
	scanf("%d",&r);
	area=3.14*r*r;
	printf("area of circle = %.2f\n",area);
	 
	printf("\nEnter length & breadth rectangle : ");
	scanf("%d,%d",&l,&b);
	area=l*b;
	printf("area of rectangle = %.2f\n",area);
	
	printf("\nEnter base & height triangle : ");
	scanf("%d,%d",&b,&h);
	area=b*h;
	printf("area of triangle = %.2f\n",area);
	
}