#include<iostream>
using namespace std;

class Matrix{
	
	int a[3][3];
	 
	public:
		
	void accept();
	void display();
	void operator + (Matrix o);
};

void Matrix::accept()
{
	cout<<endl;
	
	for(int i=0;i<3;i++)
	{
	    for(int j=0;j<3;j++)
	    {
		    cout<<"\t";
		    cin>>a[i][j];
     	}
    }
}

void Matrix::display()
{
	for(int i=0;i<3;i++)
	{
		for(int j=0;j<3;j++)
		{
			cout<<"    "<<a[i][j];
		}
		
		cout<<endl;
	}
}

void Matrix::operator + (Matrix o)
{
	long mat[3][3];
	
    for(int i=0;i<3;i++)
	{
		for(int j=0;j<3;j++)
		{
			mat[i][j] = a[i][j] + o.a[i][j]; 
		}
		
	}
	
	cout<<endl;
	
	cout<<"......................"<<endl<<endl;
	cout<<"ADDITION OF two MATRIX"<<endl<<endl;
	cout<<"......................"<<endl<<endl;
	
	for(int i=0;i<3;i++)
	{
		for(int j=0;j<3;j++)
		{
			cout<<"    "<<mat[i][j];
		}
		
		cout<<endl;
	}
}

int main()
{
	Matrix m,n;
	
	cout<<endl;
	cout<<"......................"<<endl<<endl;
	cout<<"ENTER MATRIX 1"<<endl<<endl;
	cout<<"......................"<<endl;
	m.accept();
	
	cout<<endl<<endl;
	cout<<"MATRIX NO 1 ARE"<<endl<<endl;
	m.display();
	cout<<endl;
	
	cout<<"......................"<<endl<<endl;
	cout<<"ENTER MATRIX 2"<<endl<<endl;
	cout<<"......................"<<endl;
	n.accept();
	cout<<endl;
	
	cout<<"MATRIX NO 2 ARE"<<endl<<endl;
	n.display();
	m+n;
	
	return 0;
}