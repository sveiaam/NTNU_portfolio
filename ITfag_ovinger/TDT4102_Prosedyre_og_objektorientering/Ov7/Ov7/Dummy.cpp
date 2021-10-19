#include "Dummy.h"
#include <iostream>

void dummyTest() {
	using namespace std;
	Dummy a;
	*a.num = 4;
	Dummy b(a);
	Dummy c;
	c = a;

	cout << "a: " << *a.num << endl;
	cout << "b: " << *b.num << endl;
	cout << "c: " << *c.num << endl;

	*b.num = 3;
	*c.num = 5;

	cout << "a: " << *a.num << endl;
	cout << "b: " << *b.num << endl;
	cout << "c: " << *c.num << endl;

	cin.get();
}


