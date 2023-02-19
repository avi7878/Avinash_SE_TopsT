#include<iostream>
using namespace std;

class account 
{
	int acno;
	string name;
	float bal;
	string type;
	public :
		
		void getdata()
		{
			cout<<"\nEnter the Account Number : ";
			cin>>acno;
			cout<<"\nEnter the Name : ";
			cin>>name;
			cout<<"\nEnter the Balance : ";
			cin>>bal;
			cout<<"\nEnter the type of Account : ";
			cin>>type;
		}
		void withdraw();
		void deposit();
		void display();
};

void account :: withdraw()
{
	int x;
	cout<<"Enter the value you want to withdraw : ";
	cin>>x;
	if(x<bal)
	  bal=bal-x;
	else
	  cout<<"Not enough balance : ";
}
void account :: deposit()
{
	int x;
	cout<<"Enter the amount you want to Deposit : ";
	cin>>x;
	bal=bal+x;
}
void account :: display()
{
	cout<<"\nAccount no : "<<acno;
	cout<<"\nName : "<<name;
	cout<<"\nBalance : "<<bal;
	cout<<"\nAccount : "<<type;
}
int main()
{
	account a;
	int ch;
	do
	{
		cout<<"\n==================================";
		cout<<"\nMENU";
		cout<<"\n1.Enter New Account.";
		cout<<"\n2.Withdraw.";
		cout<<"\n3.Deposit.";
		cout<<"\n4.Display.";
		cout<<"\n5.Exit.";
		cout<<"\n=================================";
		cout<<"\nEnter your Choice : ";
		
		cin>>ch;
		switch(ch)
		{
			case 1 :
				a.getdata();
				break;
			case 2 :
				a.withdraw();
				break;
			case 3 :
				a.deposit();
				break;
			case 4 :
				a.display();
				break;
			case 5 :
				exit(0);
				break;
		}
	}
	while(ch!=5);
	return 0;
}











