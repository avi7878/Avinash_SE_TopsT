#include<stdio.h>

void main()
{
	int rollno[5];
	int i,j,t;
	
    printf("\n\n\t\t\xB2\xB2\xB2\xB2\xB2\xB2\xB2 Element of Array \xB2\xB2\xB2\xB2\xB2\xB2\xB2\n\n");
    for(i=0;i<5;i++) 
    {
    	printf("\t\tEnter Element [%d] : ",i);
    	scanf("%d",&rollno[i]);
	}
	printf("\n\n\t\t\xB2\xB2\xB2\xB2\xB2\xB2\xB2 Element of Array \xB2\xB2\xB2\xB2\xB2\xB2\xB2\n\n");
	for(i=0;i<5;i++)
	{
		printf("\t\tElement of Index [%d] : %d\n",i,rollno[i]);
	}
	printf("\n\n\t\t\xB2\xB2\xB2\xB2\xB2\xB2\xB2 Array Elements in Ascending Order : \xB2\xB2\xB2\xB2\xB2\xB2\xB2\n\n");
    
    for(i=0;i<5;i++)
    {
    	for(j=i+1;j<5;j++)
    	{
    		if(rollno[i]>rollno[j])
    		{
    			t = rollno[i];
    			rollno[i] = rollno[j];
    			rollno[j] = t;
			}
		}
	}
	
	for(i=0;i<5;i++)
	{
		printf("\n\t\tElement at Index [%d] : %d",i,rollno[i]);
	}
	printf("\n\n\t\t\xB2\xB2\xB2\xB2\xB2\xB2\xB2 Array Element in Descending Order : \xB2\xB2\xB2\xB2\xB2\xB2\xB2\n\n");
	
	for(i=0;i<5;i++)
	{
		for(j=i+1;j<5;j++)
		
		{
			if(rollno[i]<rollno[j])
			{
			   	t = rollno[i];
				rollno[i] = rollno[j];
				rollno[j] = t;
		    }
		}
	}
		for(i=0;i<5;i++)
	{
		printf("\n\t\tElement at Index [%d] : %d",i,rollno[i]);
	}
	
}
	