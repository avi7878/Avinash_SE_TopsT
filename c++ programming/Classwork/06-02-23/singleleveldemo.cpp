#include<iostream>
using namespace std;

class A
{
	public:
		int a;
		
		void getA(int x)
		{
			a = x;
		}
		
		void showA()
		{
			cout<<"\nA = "<<a;
		}
};

class B : public A
{
	public:
		int b;
		
		void getB(int y)
		{
			b = y;
		}
		
		void showB()
		{
			cout<<"\nB = "<<b;
		}
};

int main()
{
	B b;
	int x,y;
	
	b.getA(x);
	cout<<"\nEnter the value of x : ";
	cin>>x;
	b.getB(y);
	cout<<"\nEnter the value of y : ";
	cin>>y;
	b.showA();
	b.showB();
}