#include<iostream>
using namespace std;

class Side{
	protected:
		double l;
	public: 
	    void getVal(int x)
	    {
	    	l = x;
		}
};

class square : public Side
{
	public: 
	        int sqr()
	        {
	        	return l*l;
			}
};

class cube : public Side 
{
	public: 
	    int cu()
	    {
	    	return l*l*l;
		}
};

int main()
{
	int a,b;
	square obj;
	cout<<"Enter the value : ";
	cin>>a;
	obj.getVal(a);
	cout<<"\nsquare is : "<<obj.sqr();
	
	cube cb;
	cout<<"\n
	Enter the value : ";
	cin>>b;
	cb.getVal(b);
	cout<<"\ncube is : "<<cb.cu();
	
	return 0;
}