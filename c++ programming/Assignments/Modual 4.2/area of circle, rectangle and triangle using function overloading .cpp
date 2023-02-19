/*Write a program to calculate the area of circle, rectangle and triangle using Function Overloading */

#include<iostream>
using namespace std;

void circle(float r)
{
	float area;
	//public :
		area = 3.14*r*r;
		cout<<"Area of Circle : "<<area;
}
void rectangle(int length,int breadth)
{
	int area;
    
    area = length*breadth;
    cout<<"Area of Rectangle : "<<area;
}
void triangle(int Base,int Height)
{
	int area;
	area = (Base * Height) / 2;
	cout<<"Area of Triangle : "<<area;
}


int main()
{
	int a,l,b,base,height;
	cout<<"\nEnter the Area : ";
	cin>>a;
	cout<<"___________________________\n";
	circle(a);
	cout<<"\n===========================";
	cout<<"\n\nEnter the Length : ";
	cin>>l;
	cout<<"Enter the Breadth : ";
	cin>>b;
	cout<<"__________________________\n";
	rectangle(l,b);
	cout<<"\n==========================\n";
	cout<<"\nEnter the Base : ";
	cin>>base;
	cout<<"Enter the Height : ";
	cin>>height;
	cout<<"_________________________\n";
	triangle(base,height);
	cout<<"\n=========================";
	return 0;
}