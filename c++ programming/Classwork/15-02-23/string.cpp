#include<iostream>
using namespace std;

int main()
{
	string fname;
	string lname;
	
	cout<<"\nEnter your FName : ";
	getline(cin,fname);
	cout<<"FName is : "<<fname;
///	lname=fname;
    cout<<"\nEnter your LName : ";
    getline(cin,lname);
	cout<<"LName is : "<<lname;
	cout<<"\nString Concatenate : "<<(fname+lname);
	int len = fname.size()+lname.size();
	cout<<"\nString Length is : "<<len;
	
	return 0;
} 