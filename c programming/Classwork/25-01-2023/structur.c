#include<stdio.h>

struct Student
{
	int eid;
	char name[20];
	float persanteg;
};

void main()
{
	struct Student a1;
	printf("\nEnter Student Id : ");
	scanf("%d",&a1.eid);
	printf("Enter Student Name : ");
	scanf("%s",&a1.name);
	printf("Enter Student Persanteg : ");
	scanf("%f",&a1.persanteg);
	
	printf("\nStudent Id : %d",a1.eid);
	printf("\nStudent Name : %s",a1.name);
	printf("\nStudent Persanteg : %.2f",a1.persanteg);
	
}