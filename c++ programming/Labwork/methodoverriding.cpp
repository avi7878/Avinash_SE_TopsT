#include<iostream>
using namespace std;

class A
{
	public :
		void show()
		{
			cout<<"\nShow for A.";
		}
};

class B : public A
{
	public :
		void show()
		{
			cout<<"\nShow for B.";
		}
};

class C : public B, public A
{
	public :
		void show()
		{
			cout<<"\nShow for C.";
		}
};
int main()
{
	C obj;
	obj.show();
	return 0;
}