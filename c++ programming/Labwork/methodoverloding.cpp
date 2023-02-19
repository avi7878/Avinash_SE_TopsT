#include<iostream>
using namespace std;

class A
{
	public :
		int a,b;
		void add()
		{
			cout<<"\nEnter A , B : ";
			cin>>a>>b;
			cout<<"\nAddition : "<<(a+b);
		}
		
		void add(int a, int b)
		{
			cout<<"\nAddition for main() : "<<(a+b);
		}
		int add(int x,int y,int z)
		{
		    return x+y+z;
		}
};

int main()
{
	A obj;
	obj.add();
	obj.add(5,6);
	cout<<"\nAdd : "<<obj.add(1,2,3);
	return 0;
}