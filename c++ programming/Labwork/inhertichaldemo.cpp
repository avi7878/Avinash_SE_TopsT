#include<iostream>
using namespace std;

class Side
{
	protected :
		   double l;
    public : 
		   void getVal(int x)
		   {
		   	   l = x;
		   }
};

class Square : public Side
{
	public : 
	       int sqr()
	       {
	       	    return l*l;
		   }
};

class Cube : public Side
{
	public :
		int cu()
		{
		    return l*l*l;
		}
};


int main()
{ 
    int a,b;
    cout<<"\nValue of the Square : ";
    cin>>a;
    cout<<"Value of the Cube : ";
    cin>>b;
    Square obj;
    obj.getVal(a);
    cout<<"\nsquare is : "<<obj.sqr();
    
    Cube cb;
 
    cb.getVal(b);
    cout<<"\nCube is : "<<cb.cu();
    
	return 0;
}