#include<iostream>
using namespace std;

class Fandemo
{
	public :
		virtual void Onbutton();
		void light()
		{
			cout<<"\nLight is on.";
		}
};

class Start : public Fandemo
{
	public :
		void Ac()
		{
			cout<<"\nAc Started.";
		}
		void Onbutton()
		{
			cout<<"\nFan is Rotating.";
		}
};
int main()
{
	Start ac;
	ac.Ac();
	ac.light();
	ac.Onbutton();
	return 0;
}