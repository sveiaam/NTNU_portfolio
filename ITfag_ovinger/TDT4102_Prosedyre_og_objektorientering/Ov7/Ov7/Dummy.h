#pragma once
#include <algorithm>

class Dummy
{
public:
	int *num;
	Dummy() {
		num = new int(0);
	}

	~Dummy() {
		delete num;
	}

	Dummy(const Dummy &a) {
		this->num = new int(*a.num);
	}

	Dummy &operator = (Dummy a) {
		std::swap(num, a.num);
		return *this;
	}
};

void dummyTest();
