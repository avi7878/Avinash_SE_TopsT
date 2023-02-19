//Write a program of Addition, Subtraction, Division, Multiplication using constructor.

#include<iostream>
using namespace std;

class A
{
	public :
		int add,sub,mul;
		float div;
		A(int x,int y)
		{
			add=x+y;
			sub=x-y;
			mul=x*y;
		    div=x/y;
		}
		void display()
		{
			cout<<"\nAddition is : "<<add;
			cout<<"\nSubtraction is : "<<sub;
			cout<<"\nMultipication is : "<<mul;
			cout<<"\nDivision is : "<<(float)div;
		}
};

int main()
{
	int a,b;
	cout<<"\nEnter the two Values : ";
	cin>>a>>b;
	A obj(a,b);
	obj.display();
//	obj.A(5,4);
	return 0;
} 