#include<iostream>
using namespace std;

class Student
{
	public :
		string name;
		int rollno;
		void getname(string n)
		{
			name = n;
		}
		Student(int r)
		{
		    rollno = r;	
	    }
};

class Extramarks
{
	public :
		int sp;
		Extramarks(int s)
		{
			sp = s;
		}
};

class Result : public Student,public Extramarsks
{
    public :
	    int s1,s2,s3,tot;
		float per;	
		Result()
		{
			s1 = x;
			s2 = y;
			s3 = z;
			tot = s1+s2+s3+sp;
			per = (float)tot/4;
		}
};
int main()
{
	return 0;
}