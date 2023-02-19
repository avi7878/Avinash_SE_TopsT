/*Create a class person having members name and age. Derive a class student 
having member percentage. Derive another class teacher having member 
salary. Write necessary member function to initialize, read and write data. 
Write also Main function (Multiple Inheritance)*/

#include<iostream>
using namespace std;

class Person
{
	public :
		int age;
		string name;
		Person()
		{
			name = "Avinash chauhan";
			age = 21;
		}
};

class Student : public Person
{
	public :
		Student()
		{	
		}
};

class Teacher : public Student
{
};

int main()
{
	return 0;
}