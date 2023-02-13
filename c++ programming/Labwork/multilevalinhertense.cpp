#include<iostream>
using namespace std;

class A
{
	public :
		int d;
		void getA(int x)
		{
			d = x;
		}
		
		void showA()
		{
			cout<<"\nD = "<<d;
		}
};

class B : public A
{
	public :
		int e;
		void getB(int y)
		{
			e = y;
		}
		void showB()
		{
			cout<<"\nE = "<<e;
		}
};

class C : public B
{
	public :
		int f;
		void getC(int z)
		{
			f = z;
		}
		void showC()
		{
			cout<<"\nF = "<<f;
		}
};

int main()
{
	int a,b,c;
	cout<<"\nEnter the D : ";
	cin>>a;
	cout<<"\nEnter the E : ";
	cin>>b;
	cout<<"\nEnter the F : ";
	cin>>c;
	
	C obj;
	obj.getA(a);
	obj.getB(b);
	obj.getC(c);
	obj.showA();
	obj.showB();
	obj.showC();
	return 0;
}