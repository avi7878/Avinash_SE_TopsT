#include<iostream>
using namespace std;

class MO
{
   public :
        
		void add()
		{
			int a,b;
		    cout<<"\nEnter A , B :" ;
			cin>>a>>b;
			cout<<"\nAddition : "<<(a+b);	
		}
		void add(int a, int b)
		{
		    cout<<"\nAddition From main() : "<<(a+b);	
		}	
		
		int add(int x,int y,int z)
		{
			return x+y+z;
		}
};
int main()
{
	MO obj;
	obj.add();
	obj.add(4,5);
	cout<<"\nAdd : "<<obj.add(3,3,3);
	return 0;
}