/*Assume a class cricketer is declared. Declare a derived class batsman from 
cricketer. Data member of batsman. Total runs, Average runs and best 
performance. Member functions input data, calculate average runs, Display 
data. (Single Inheritance)*/

#include<iostream>
using namespace std;

class Cricketer
{
	public :
		int tr,averun,bestper,tm,jn,age;
		string name,role;
		
		Cricketer()
		{
			name = "Rohit sharma";
			role = "Indian team";
			tr = 50236;
			tm = 445;
			jn = 45;
			age = 35;
			averun = 90;
			bestper = 212;
			
		}
};

class Batsman : public Cricketer
{
	public :
    	void Information()
	    {
	    	cout<<"\nBATSMAN DETAILS.";
	    	cout<<"\n\nBatsman Name : "<<name;
	    	cout<<"\nTeam Name : "<<role;
	    	cout<<"\nJersey No : "<<jn;
	    	cout<<"\nbatsman Age : "<<age;
		
     	}
     	void Display()
     	{
     		cout<<"\n==========================";
     		cout<<"\nCRICKET CAREER.";
     		cout<<"\n\nName : "<<name;
     		cout<<"\nMatch played : "<<tm;
     		cout<<"\nTotal Run : "<<tr;
     		cout<<"\nAverag : "<<averun;
     		cout<<"\nBest score : "<<bestper;
     		
		}
};

int main()
{
	Batsman obj;
	obj.Information();
	obj.Display();
	return 0;
}
	
	
	
	
	