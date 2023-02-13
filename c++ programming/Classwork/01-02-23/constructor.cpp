#include<iostream>
using namespace std;

class Sample
{
	public:
		Sample()
		{
		     cout<<"\nDefault constructor called.";	
		}	
		void show()
		{
			cout<<"\nThis is a Show Method.";
		}
};

int main()
{
	Sample obj1;
	obj1.show();
	return 0;
}