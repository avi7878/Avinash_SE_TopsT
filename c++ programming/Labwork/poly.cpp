#include<iostream>
using namespace std;

class OM
{
	public :
		int a,b;
		void add()
		{
			cout<<"\nEnter A , B : ";
			cin>>a>>b;
			cout<<"\nAddition : "<<(a+b);
		}
};
int main()
{
	OM obj;
	obj.add();
	return 0;
}