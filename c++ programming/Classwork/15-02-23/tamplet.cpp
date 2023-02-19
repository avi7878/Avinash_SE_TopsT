#include<iostream>
using namespace std;

template <typename T>
T common(T a,T b)
{
	return a+b;
}


int main()
{
	cout<<"\nAdd using int : "<<common<int>(5,7);
	cout<<"\nString Concatenation : "<<common<string>("avi", "chauhan");
	cout<<"\nAdd using Float : "<<common<float>(4.5f,4.5f);
	return 0;
}