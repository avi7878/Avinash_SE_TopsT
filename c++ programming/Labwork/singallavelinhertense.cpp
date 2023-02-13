#include<iostream>
using namespace std;

class A
{
	public :
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
	public :
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
/*	A obj1;
	obj1.getA(5);
	obj1.showA();
	B obj2;
	obj2.getB(2);
	obj2.showB();
	return 0;
*/

    int a,b;
    
    cout<<"\nEnter the A : ";
    cin>>a;
    cout<<"\nEnter the B : ";
    cin>>b;
    B obj;
    obj.getA(a);
    obj.getB(b);
    obj.showA();
    obj.showB();
    
}