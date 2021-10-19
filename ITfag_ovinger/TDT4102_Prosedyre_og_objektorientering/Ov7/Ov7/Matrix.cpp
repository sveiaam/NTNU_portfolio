#include "Matrix.h"
#include <iostream>
#include <iomanip>
#include <algorithm>

Matrix::Matrix()
{
	arr = nullptr;
	rows = 0;
	columns = 0;
};

Matrix::Matrix(int nRows, int nColumns) {
	rows = nRows;
	columns = nColumns;
	arr = new double*[nRows] {0};
	for (int i = 0; i < nRows; i++) {
		arr[i] = new double[nColumns] {0};
	};
};

Matrix::~Matrix()
{
	for (int i = 0; i < rows; i++) {
		delete[] arr[i];
	};
	delete[] arr;
	arr = nullptr;
};

double Matrix::get(int row, int col) const {
	return arr[row][col];
};
void Matrix::set(int row, int col, double value) {
	arr[row][col] = value;
};

int Matrix::getHeight() const {
	return rows;
};
int Matrix::getWidth() const {
	return columns;
};

bool Matrix::isValid() const {
	if (arr == nullptr) {
		return false;
	}
	else {
		return true;
	};
};

std::ostream &operator << (std::ostream &os, const Matrix &A) {
	if (A.isValid()) {
		int m = A.getHeight();
		int n = A.getWidth();
		for (int i = 0; i < m; i++) {
			for (int j = 0; j < n; j++) {
				os << std::setw(4) << A.get(i, j);
			};
			os << "\n";
		};
	}
	else {
		os << "### Invalid matrix ###\n";
	};
	return os;
};

//Copy-constructor
Matrix::Matrix(const Matrix &rhs) { 
	if (rhs.isValid()) {
		int m = rhs.getHeight();
		int n = rhs.getWidth();
		//allocate new memory
		this->arr = new double*[m] {0};
		for (int i = 0; i < m; i++) {
			arr[i] = new double[n] {};
		};
		//copy each element
		this->rows = m;
		this->columns = n;
		for (int i = 0; i < m; i++) {
			for (int j = 0; j < n; j++) {
				this->set(i, j, rhs.get(i, j));
			};
		};
	}
	else {
		this->arr = nullptr;
	};
};

// = operator
Matrix &Matrix::operator = (Matrix A) {
	std::swap(*this, A);
	return *this;
}

// += operator
Matrix &Matrix::operator += (const Matrix& A) {
	int m = this->getHeight();
	int n = this->getWidth();
	if ((m == A.getHeight()) and (n == A.getWidth()) and (this->isValid()) and (A.isValid())) {
		for (int i = 0; i < m; i++) {
			for (int j = 0; j < n; j++) {
				this->set(i, j, this->get(i, j) + A.get(i, j));
			};
		};
		return *this;
	}
	else {
		this->arr = nullptr;
		return *this;
	};
};
// + operator
Matrix Matrix::operator + (const Matrix &A) {
	Matrix result = Matrix(*this);
	result += A;
	return result;
};
// -= operator
Matrix &Matrix::operator -= (const Matrix &A) {
	int m = this->getHeight();
	int n = this->getWidth();
	if ((m == A.getHeight()) and (n == A.getWidth()) and (this->isValid()) and (A.isValid())) {
		for (int i = 0; i < m; i++) {
			for (int j = 0; j < n; j++) {
				this->set(i, j, this->get(i, j) - A.get(i, j));
			};
		};
		return *this;
	}
	else {
		this->arr = nullptr;
		return *this;
	};
};
// - operator
Matrix Matrix::operator - (const Matrix &A) {
	Matrix result = Matrix(*this);
	result -= A;
	return result;
};
// *= operator
Matrix &Matrix::operator *= (const Matrix &A) {
	int m = this->getHeight();
	int n = this->getWidth();
	double temp;
	Matrix result = Matrix(m, m);
	if ((n == A.getHeight()) and (m == A.getWidth()) and (this->isValid()) and (A.isValid())) {
		for (int i = 0; i < m; i++) {
			for (int j = 0; j < n; j++) {
				temp = 0.0;
				for (int k = 0; k < n; k++) {
					temp += (this->get(i, k)) * (A.get(k, j));
				};
				result.set(i, j, temp);
			};
		};
		std::swap(result, *this);
		return *this;
	}
	else {
		this->arr = nullptr;
		return *this;
	};
};
// * operator
Matrix Matrix::operator * (const Matrix &A) {
	Matrix result = Matrix(*this);
	result *= A;
	return result;
}

