#include<iostream>

using namespace std;


class Demo{
	public:
		void func();
};

void Demo::func()
{
	cout<<"\nFunction Implemented outside the class.";
}
int main()
{
	Demo obj;
	obj.func();
	return 0;
}