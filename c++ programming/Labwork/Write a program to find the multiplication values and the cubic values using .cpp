#include<iostream>
using namespace std;

class Line
{
	public :
		float a,b;
		inline float mul(float c,float d)
		{
			a=c;
			b=d;
			return (a*b);
		}
		inline float cub(float a)
		{
			return (a*a*a);
		}
		void Display()
		{
			cout<<"\nMultipliction : "<<(a*b);
			cout<<"\nCubic : "<<a*a*a;
		}
};
int main()
{
	float x,y;
	cout<<"\nEnter two values : ";
	cin>>x>>y;
	Line a;
	a.mul(x,y);
	a.Display();
	return 0;
}