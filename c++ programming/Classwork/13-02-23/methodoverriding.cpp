#include<iostream>
using namespace std;

class A 
{
	public :
		void show()
		{
			cout<<"\nShow for A";
		}
};
class B : public A
{
	public : 
	    void show()
	    {
	    	A::show();
	    	cout<<"\nShow for B";
		}
};
class C : public B
{
	public :
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