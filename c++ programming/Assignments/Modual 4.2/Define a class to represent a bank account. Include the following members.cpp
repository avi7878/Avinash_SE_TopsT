/* Define a class to represent a bank account. Include the following members: 
1. Data Member: 
-Name of the depositor 
-Account Number 
-Type of Account 
-Balance amount in the account 
2. Member Functions 
-To assign values 
-To deposited an amount 
-To withdraw an amount after checking balance 
-To display name and balance
*/

#include<iostream>
using namespace std;

class Bank
{
	public :
	int acntno,amount;
	string name,type;
	
	Bank(int a, int m, string n, string t)
	{
		acntno = a;
		amount = m;
		name = n;
		type = t;
	}
	void Display()
	{
		cout<<"\nAccount Number is "<<acntno;
		cout<<"\nAmount is "<<amount;
		cout<<"\nName is "<<name;
		cout<<"\nAccount type is "<<type;
	}
	
};

int main()
{
	string ac,saving;
//	int 123,200;
	
	Bank obj(123,200,ac,saving);
//	obj.Bank;
	obj.Display();
	return 0;
}