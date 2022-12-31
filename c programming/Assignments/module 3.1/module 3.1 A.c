#include<stdio.h>

void main()
{
	int age;
	char name[10];
	float date;
	char address;
	printf("\n\n\n\n\n\n\t\t\xB2\xB2\xB2\xB2\xB2 Accept personal Details \xB2\xB2\xB2\xB2\xB2");
	printf("\n\n\t\tEnter your Name : ");
	scanf("%s",&name);
	fflush(stdin);
	printf("\t\tEnter your Birth Date : ");
	scanf("%f",&date);
	printf("\t\tEnter your Age : ");
	scanf("%d",&age); 
	printf("\t\tEnter your address : ");
	scanf("%s,&address");
	printf("\n\n\n\t\t\t\xB2\xB2\xB2\xB2\xB2 Show personal Details \xB2\xB2\xB2\xB2\xB2");
	printf("\n\n\t\tName : %s", name);
	printf("\n\n\t\tDate : %f", date);
	printf("\n\n\t\tAge : %d", age);
	printf("\n\n\t\tAddress : .%s", address);
	
}