#include<iostream>
using namespace std;

class student
{
	public :
    int rollno,s1,s2,s3,tot;
};

int main()
{
	int i;
    student obj;
//	cout<<"Enter Rollno : ";
//	cin>>obj.rollno;
	for(i=0;i<3;i++)
	{
		cout<<"Enter Rollno,s1,s2,s3\n";
		cin>>obj.rollno>>obj.s1>>obj.s2>>obj.s3;
	}
	return 0;
}