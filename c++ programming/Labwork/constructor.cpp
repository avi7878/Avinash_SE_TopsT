#include<iostream>
using namespace std;

class simple
{
	public :
		simple()
		{
			cout<<"Defualt constructor called.";
		}
		void show()
		{
			cout<<"\nThis is show method.";
		}
};

int main()
{
	simple obj;
	obj.show();
	return 0;
}