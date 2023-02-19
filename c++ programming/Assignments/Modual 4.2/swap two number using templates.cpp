/* Write a program of to swap the two values using templates*/

#include<iostream>
using namespace std;

template<typename s>
s swap (s a,s b)
{
	int c;
	cout<<"\nBefore Swapping A = "<<a<<"\tB = "<<b;
	
	c = a;
	a = b;
	b = c;
	
	cout<<"\nAfter Swapping A = "<<a<<"\tB = "<<b;
	
	return 0;
	
}
int main()
{
	swap(5,6);
	return 0;
}