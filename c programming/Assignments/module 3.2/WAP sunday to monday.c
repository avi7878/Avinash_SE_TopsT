#include<stdio.h>

void main()
{
	int day;
	
	printf("Enter the Number : ");
	scanf("%d",&day);
    
	
	switch(day) 
	{
	    case 1:
	    printf("Monday");
		break;
		case 2:
		printf("Tuesday");
		break;
		case 3:
	    printf("Wednesday");
	    break;
	    case 4:
	    printf("thrusday");
	    break;
	    case 5:
	    printf("Friday");
	    break;
	    case 6:
	    printf("saturday");
	    break;
	    case 7:
	    printf("Sunday");
	    break;
	    default:
	    printf("Invalid Number");
	    break;
				
	}
}