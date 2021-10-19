#pragma once
#include <iostream>

class Matrix
{
public:
	//standard constructor
	Matrix();
	//constructs nRows x nColumns 0 matrix
	Matrix(int nRows, int nColumns);
	//constructs the nRows x nRows identity matrix
	explicit Matrix(int nRows) : Matrix(nRows, nRows) {
		//Has run the 0-constructor. Now insert 1's on the diagonal:
		for (int i = 0; i < nRows; i++) {
			arr[i][i] = 1;
		};
	};
	//destructor
	~Matrix();

	//getters and setters
	double get(int row, int col) const;
	void set(int row, int col, double value);
	int getHeight() const;
	int getWidth() const;
	bool isValid() const;
	
	// << overloading
	friend std::ostream &operator << (std::ostream &os, const Matrix &A);

	//copying
	Matrix(const Matrix &rhs);

	// = operator
	Matrix &operator = (Matrix A);

	// += operator
	Matrix &operator += (const Matrix &A);
	// + operator
	Matrix operator + (const Matrix &A);
	// -= operator
	Matrix &operator -= (const Matrix &A);
	// - operator
	Matrix operator - (const Matrix &A);
	// *= operator
	Matrix &operator *= (const Matrix &A);
	// * operator
	Matrix operator * (const Matrix &A);


private:
	int rows;
	int columns;
	double **arr;
};
