/*Write a program to find the max number from given two numbers using friend function */

#include<iostream>
using namespace std;

class Add
{
	int a,b;
	friend void Ab(Add);
	public :
		void Ac()
		{
			cout<<"\nEnter First Number : ";
			cin>>a;
			cout<<"Enter Second Number : ";
			cin>>b;
		}
};

void Ab(Add obj)
{
    if (obj.a > obj.b)
    {
    	cout<<"=========================\n";
        cout << "Max Number is : " <<obj.a;
    }
    else
    {
    	cout<<"=========================\n";
        cout << "Max Number is : " <<obj.b;
    }
}

int main()
{
	Add obj;
	obj.Ac();
	Ab(obj);
	return 0;
}