#include<iostream>
using namespace std;

int add(int a,int b)
{
	return a+b;
}
int sub(int c,int d)
{
	return c-d;
}
int multi(int e,int f)
{
	return e*f;
}
int divi(int g,int h)
{
	return g/h;
}
int main()
{
	int i,j,sum,choice;
	
	cout<<"Enter the I : ";
	cin>>i;
	cout<<"Enter the J : ";
	cin>>j;
	
	cout<<"\nStart Function.";
	
	cout<<"\nPress 1 to Addition.\n";
	
	cout<<"\nPress 2 to Subtrection.\n";
	
	cout<<"\nPress 3 to Multipliction.\n";
	
	cout<<"\nPress 4 to Division.\n";
	
	cout<<"\nEnter your choice? : ";
	cin>>choice;
	
	switch(choice)
	{
		case 1:
	    	sum=add(i,j);
	    	cout<<"\nAddition is : "<<sum;
	    	break;
		case 2:
	    	sum=sub(i,j);
		    cout<<"\nSubtrection is : "<<sum;
	    	break;
		case 3:
			sum=multi(i,j);
			cout<<"\nMultiplication is : "<<(float)sum;
			break;
		case 4: 
		    sum=divi(i,j);
		    cout<<"\nDivision is : "<<sum;
		    break;
		default : cout<<"Invalid Number.";
		
	}
	
}





