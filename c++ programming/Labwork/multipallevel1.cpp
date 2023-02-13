#include<iostream>
using namespace std;

class Student 
{
	public :
		string name;
		int rollno;
		
		void getname(string n, int r)
		{
			name = n;
			rollno = r;
		}
//		Student(const Student&obj ,int r)
//		{
//			rollno = r;
//		}
};
class Extramarks
{
	public :
		int sp;
		
		Extramarks()
		{
			sp = 60;
		}
};

class Result : public Student,public Extramarks
{   
   public :
       int s1,s2,s3,tot;
	   float per;
	   
	   Result(int x,int y,int z)
	   {
	        s1 = x;
			s2 = y;
			s3 = z;
			tot = s1+s2+s3+sp; 
			per = (float)tot/4;  	
	   }	
	   void Display()
	   { 
	        cout<<"\nName : "<<name;
	        cout<<"\nRollno : "<<rollno;
	        cout<<"\nTotal : "<<tot;
	        cout<<"\nPercentage : "<<per;
	   	    
	   }
};

int main()
{ 
    
    int s1,s2,s3,sp,rollno;
    string name;
    
    cout<<"\nEnter Your Name : ";
    getline(cin,name);
    cout<<"\nEnter Your RollNo : ";
    cin>>rollno;
	cout<<"\nEnter Your physics Marks : ";
	cin>>s1;
	cout<<"\nEnter Your chemistry Marks : ";
	cin>>s2;
	cout<<"\nEnter Your maths Marks : ";
	cin>>s3;
	cout<<"\nEnter Your sports Marks : 60";
//	cin>>sp;
	Result obj(s1,s2,s3);
	obj.getname(name,rollno);
//	obj.Student(rollno);
//   obj.Extramarks(sp);
	obj.Display();
	                  
	
	                  
	

	
    
	return 0;
}