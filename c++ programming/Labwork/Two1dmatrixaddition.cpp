/* Write a Program of Two 1D Matrix Addition using Operator Overloading */

#include<iostream>
using namespace std;

class A
{
	public :
	int matrix1[3];
	
    	int i;
        void D()
    	{
    		cout<<"\nElement of Matrix1\n\n";
    		for(i=0;i<3;i++)
        	{
        		cout<<"Enter Element" <<i; " : ";
        		cout<<" : ";
        		cin>>matrix1[i];
	    	}
    	}
//    	
//    	void Display()
//    	{
//    		cout<<"\nMatrix1\n";
//    		for(i=0;i<3;i++)
//    		{
//    			cout<<"\t";
//    			cout<<matrix1[i];
//			}
//		}
};

class B : public A
{
	int matrix2[3];
	public :
		void E()
		{
			cout<<"\nElement of Matrix2\n\n";
			for(i=0;i<3;i++)
			{
				cout<<"Enter Element"<<i;
				cout<<" : ";
				cin>>matrix2[i];
			}
		}
		
		void Display()
		{
			    	
   
    		cout<<"\nMatrix1\n";
    		for(i=0;i<3;i++)
    		{
    			cout<<matrix1[i];
    			cout<<"\t";
			}
		
            cout<<"\n\nMatrix2\n";
			for(i=0;i<3;i++)
			{
				cout<<matrix2[i];
				cout<<"\t";
			}
			
			cout<<"\n\nAddition of two Matrix\n";
			for(i=0;i<3;i++)
			{
			cout<<matrix1[i]+matrix2[i]<<"\t";
		    }
		}
		
};

int main()
{
    B obj;
    obj.D();
    obj.E();
    obj.Display();
	return 0;
}