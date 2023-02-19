#include<iostream>
using namespace std;

class Maths
{
	public :
		
		void Add(int a,int b)
		{
			cout<<"\nAddition : "<<a+b;
		}
		
		void Sub(int a,int b)
		{
			cout<<"\nSubtrection : "<<a-b;
		}
		void mul(int a,int b)
		{
			cout<<"\nMultiplication : "<<a*b;
		}
		int Div(int a,int b)
		{
			cout<<"\nDivison : "<<(float)a/b;
			return 0;
		    
		}
};

int main()
{
	int x,y;
	cout<<"Enter x : ";
	cin>>x;
	cout<<"Enter y : ";
	cin>>y;
	Maths d1;
	d1.Add(x,y);
	d1.Sub(x,y);
	d1.mul(x,y);
	d1.Div(x,y);
	return 0;
}