#include<iostream>
using namespace std;

class box{
	public:
	    double width,depth,height;
	    
	box()
	{
		cout<<"\nDefault Constructor Called.";
		width = 4;
		depth = 5;
		height = 3;
	}
	
	box(double w,double h,double d)
	{
		cout<<"\n\nParameterized Constructor Called.";
		width = w;
		depth = d;
		height = h;
		
	}
	void valume()
	{
		cout<<"\nCopy Constructor.";
	}
	return 0;
};
