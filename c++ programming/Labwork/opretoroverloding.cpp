#include<iostream>
using namespace std;

class Distance
{
	public :
		int feet,inches;
		Distance(int f,int i)
		{
			feet = f;
			inches = i;
		}
		Distance operator-()
		{
			feet = -feet;
            inches = -inches;
			return Distance(feet,inches);			
		}
		void Display()
		{
			cout<<"\nFeet : "<<feet<<"\nInches : "<<inches;
		}
};

int main()
{
	int a,b;
	cout<<"\nEnter the Feet : ";
	cin>>a;
	cout<<"Enter the Inches : ";
	cin>>b;
	Distance d1(a,b);
	d1.Display();
	-d1;
	d1.Display();
	
	return 0;
}