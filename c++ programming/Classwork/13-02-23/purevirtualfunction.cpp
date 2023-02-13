#include<iostream>
using namespace std;

class FanDemo
{
	public:
		
		virtual void OnButton();
		void light()
		{
			cout<<"\nLight is On.";
		}
};

class Start : public FanDemo
{
	public :
		void Ac()
		{
			cout<<"\nAc started.";
		}
		
		void OnButton()
		{
			cout<<"\nFan is Rotating.";
		}
};
int main()
{
	Start obj;
	obj.Ac();
	obj.light();
	obj.OnButton();
	return 0;
}