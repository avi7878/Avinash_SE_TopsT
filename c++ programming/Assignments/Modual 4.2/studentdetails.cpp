/*Assume that the test results of a batch of students are stored in three different 
classes. Class Students are storing the roll number. Class Test stores the marks 
obtained in two subjects and class result contains the total marks obtained in 
the test. The class result can inherit the details of the marks obtained in the 
test and roll number of students. (Multilevel Inheritance)*/

#include<iostream>
using namespace std;

class Student 
{
	public :
 		int rollno;
	    string name;
		Student()
		{
			name = "Avinash chauhan";
			rollno = 78;
		}
};

class Test : public Student
{
	public :
		int sub1,sub2;
		Test()
		{
			sub1 = 86;
			sub2 = 78;
		}
};

class Result : public Test
{
	public :
		int sum;
		Result()
		{
			sum = sub1+sub2;
		}
		
		void Display()
		{
			cout<<"\t\t\t\xB2\xB2\xB2\xB2\xB2\xB2 STUDENT DETAILS \xB2\xB2\xB2\xB2\xB2\xB2";
			cout<<"\n\t\t\tStudent Name is : "<<name;
			cout<<"\n\t\t\tStudent RollNo is : "<<rollno;
			cout<<"\n\t\t\tSubject one Marks : "<<sub1;
			cout<<"\n\t\t\tSubject two Marks : "<<sub2;
			cout<<"\n\t\t\tTotal Marks is : "<<sum;
		}
};


int main()
{
	Result r1;
	r1.Display();
	return 0;
}
	