//Reverse a string using recursion
# include <stdio.h>

void reverse(char *str)
{
if (*str)
{
	reverse(str+1);
	printf("%c", *str);
}
}

int main()
{
char a[20];
printf("Enter the string : ");
//scanf("%s",&a);
gets(a);

reverse(a);
return 0;
}
