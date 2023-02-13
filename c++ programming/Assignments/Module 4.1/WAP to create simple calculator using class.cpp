#include<iostream>
using namespace std;

class calculator
{
    int a,b;
	
	void number()
	{
		cout<<"Enter the First number : ";
		cin>>a;
		cout<<"Enter the Second number : ";
		cin>>b;
	}
	float add()
	{
		a+b;
	}
	float sub()
	{
		a-b;
	}
	float mul()
	{
		a*b;
	}
	float div()
	{
		a/b;
	}	
};

int main()
{
	calculator c;
	cout<<"Enter 1 to addition : "<<
	"\nEnter 2 to subterction : "<<
	"\nEnter 3 to multipiction : "<<
	"\nEnter 4 to division : "<<
	"\nEnter 0 to Exit.";
    	
	return 0;
}