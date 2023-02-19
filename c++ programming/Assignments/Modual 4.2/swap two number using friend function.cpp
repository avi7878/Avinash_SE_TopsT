/*Write a program to swap the two numbers using friend function without using third variable */

#include<iostream>
using namespace std;

class A
{

		int a,b;
		friend void swap(A);
	public :
		void get()
		{
			cout<<"\nEnter 1st Number : ";
			cin>>a;
			cout<<"Enter 2nd Number : ";
			cin>>b;
		}
};
void swap(A s1)
{
	s1.a = s1.a+s1.b;
	s1.b = s1.a-s1.b;
	s1.a = s1.a-s1.b;
	cout<<"_________________________";
	cout<<"\nAfter swaping.";
	cout<<"\n_______________________";
	cout<<"\n1st Number : "<<s1.a;
	cout<<"\n2nd Number : "<<s1.b;
}
int main()
{
	A obj;
	obj.get();
	swap(obj);
	return 0;
}