#include<iostream>
using namespace std;

int main()
{
	string fname;
	string lname;
	
	cout<<"\nEnter your FName : ";
	getline(cin,fname);
	cout<<"\nFName : "<<fname;
	cout<<"\nEnter your LName : ";
	getline(cin,lname);
	cout<<"\nLName : "<<lname;
	cout<<"\nString Name Concatenat : "<<(fname+lname);
	int n = fname.size()+lname.size();
	cout<<"\nLength is : "<<n;
	return 0;
}