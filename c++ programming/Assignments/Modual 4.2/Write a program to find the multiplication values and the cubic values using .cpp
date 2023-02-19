// Write a program to find the multiplication values and the cubic values using inline function.

#include<iostream>
using namespace std;

class Line
{
	public :
		inline float mul(float x,float y)
		{
			return (x*y);
		}
		inline float cub(float g)
		{
			return (g*g*g);
		}

};
int main()
{
	float val1,val2;

	Line obj;
	cout<<"Enter the two Values : ";
	cin>>val1>>val2;
	cout<<"\nMultipliction Values is : "<<obj.mul(val1,val2);
	cout<<"\nCubic Values is : "<<obj.cub(val1)<<"\t"<<obj.cub(val2);
	return 0;
}