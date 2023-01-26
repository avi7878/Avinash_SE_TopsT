#include<stdio.h>

void reverse(char *str)
{
	if(*str)
	{
		reverse(str+1);
		printf("%c",*str);
	}
}

void main()
{
	char a[20];
	
	printf("Enter the String : ");
	gets(a);
	reverse(a);
	return 0;
}