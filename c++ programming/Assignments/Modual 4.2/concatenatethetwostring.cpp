/*Write a program to concatenate the two strings using Operator Overloading */

#include<iostream>
using namespace std;

class strg
{
	public :
		string namea,nameb;
		
		strg(string a,string b)
		{
			namea = a;
			nameb = b;
		}
		
		void operator+()
		{
			cout<<"\nConcantenate : "<<(namea+(" ")+nameb);
		}
		
};

int main()
{
	string x,y;
	cout<<"Enter the NameA : ";
	cin>>x;
	cout<<"Enter the NameB : ";
	cin>>y;
	strg obj(x,y);
	+obj;
	return 0;
}