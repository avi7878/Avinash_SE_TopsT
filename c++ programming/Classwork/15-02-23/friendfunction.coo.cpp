#include<iostream>
using namespace std;

class Avinash
{
	private :
		int money;
		friend int jyot(Avinash);
	public:
		Avinash()
		{
			money = 0;
			cout<<"\nMoney is "<<money;
		}
};

int jyot(Avinash obj)
{
	obj.money = 5000;
	return obj.money;
}
int main()
{
	Avinash avi;
	cout<<"\nMoney Given to jyot is Rs. : "<<jyot(avi);
	return 0;
}