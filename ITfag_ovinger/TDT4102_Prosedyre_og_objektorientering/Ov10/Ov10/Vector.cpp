#include "Vector.h"
#include <cmath>

void Vector::set(int row, double value) {
	this->Matrix::set(row, 0, value);
}

double Vector::get(int row) const {
	return this->Matrix::get(row, 0);
}

double Vector::dot(const Vector &rhs) const {
	if (rhs.getRows() == this->getRows()) {
		double counter = 0;
		for (int i = 0; i < this->getRows(); i++) {
			counter += rhs.get(i) * this->get(i);
		}
		return counter;
	}
	else {
		return nan("");
	}
}

double Vector::lengthSquared() const {
	return this->dot(*this);
}

double Vector::length() const {
	return sqrt(lengthSquared());
}


