#include<iostream>
using namespace std;

class calculator
{
    public :
    	int a,b,c,ch;
	     
		 void Result()
		 {
		    cout<<"\nEnter the First Number : ";
			cin>>a;
			cout<<"\nEnter the Second Number : ";
			cin>>b;
			
			cout<<"\nPress 1 to Addition.";
			cout<<"\nPress 2 to Subtrection.";
			cout<<"\nPress 3 to Multipliction.";
			cout<<"\nPress 4 to Devision"; 
			cout<<"\nEnter Your Choice? ";
			cin>>ch;
			
			    if(ch==1)
	     {
	     	c=a+b;
	     	cout<<"\nAddition is : "<<c;
		 }
		 if(ch==2)
		 {
		 	c=a-b;
		 	cout<<"\nSubtrection is : "<<c;
		 }
		 if(ch==3)
		 {
		 	c=a*b;
		 	cout<<"\nMultipliction is : "<<c;
		 }
		 if(ch==4)
		 {
		 	c=a/b;
		 	cout<<"\nDevision is : "<<c;
		 }
		 if(ch>4)
		 {
		 	cout<<"\nInvalid Input.";
		 }	
	 }
};

int main()
{
	calculator obj;
	obj.Result();
	
	
	return 0;
}