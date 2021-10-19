#pragma once
#include "Matrix.h"
class Vector :
	public Matrix
{
public:
	Vector() : Matrix() {};
	explicit Vector(int Rows) : Matrix(Rows, 1, 0.0) {};
	Vector(const Matrix & other) {
		if (other.isValid() && other.getColumns() == 1) {
			this->Matrix::operator = (other);
		}
		else {
			this->invalidate();
		}
	}
	void set(int row, double value);
	double get(int row) const;
	double dot(const Vector &rhs) const;
	double lengthSquared() const;
	double length() const;


};

