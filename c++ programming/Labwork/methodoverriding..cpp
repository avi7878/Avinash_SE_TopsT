#include<iostream>
using namespace std;

class A
{
	public :
		int a;
		void show()
		{
			cout<<"\nShow for A";
		}
};
class B : public A
{
	public :
		int b;
		void show()
		{
			A::show();
			cout<<"\nShow for B";
		}
};
class C : public B
{
	public :
		int c;
		void show()
		{
			B::show();
			cout<<"\nShow for C";
		}
};
int main()
{
	C obj;
	obj.show();
	return 0;
}