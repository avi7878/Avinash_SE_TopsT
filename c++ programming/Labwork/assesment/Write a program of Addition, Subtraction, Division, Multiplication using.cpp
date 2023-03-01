#include<iostream>
using namespace std;

class all
{
	public:
		int add,sub,div,mul;
		
		all(int x,int y)
		{
			add=x+y;
			sub=x-y;
			mul=x*y;
			div=x/y;
		}
		


		void show()
		{
			cout<<"\nAddition : "<<add;
			cout<<"\nSubtrection : "<<sub;
			cout<<"\nMultiplication : "<<mul;
			cout<<"\nDivision : "<<(float)div;
		}
	
};
int main()
{
	int a,b;
	cout<<"Enter the First Number : ";
	cin>>a;
	cout<<"Enter the Second Number : ";
	cin>>b;
    all obj(a,b);
	obj.show();	
}