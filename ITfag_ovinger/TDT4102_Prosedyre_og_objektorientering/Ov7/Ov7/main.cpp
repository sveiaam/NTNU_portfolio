#include "Oppg1.h"
#include "Matrix.h"
#include "Dummy.h"
#include <iostream>


int main() {
	// OPPG 1
	//std::cout << "\n\n\n\nOPPG 1\n\n\n\n";
	//createFibonacci();

	// OPPG 3
	//std::cout << "\n\n\n\nOPPG 3\n\n\n\n";
	//dummyTest();

	// OPPG 2, 4 og 5
	std::cout << "\n\n\n\nOPPG MATRIX\n\n\n\n";

	Matrix A = Matrix(2, 2);
	A.set(0, 0, 1.0);
	A.set(0, 1, 2.0);
	A.set(1, 0, 3.0);
	A.set(1, 1, 4.0);
	std::cout << "A:\n" << A << std::endl;

	Matrix B = Matrix(2, 2);
	B.set(0, 0, 4.0);
	B.set(0, 1, 3.0);
	B.set(1, 0, 2.0);
	B.set(1, 1, 1.0);
	std::cout << "B:\n" << B << std::endl;

	Matrix C = Matrix(2, 2);
	C.set(0, 0, 1.0);
	C.set(0, 1, 3.0);
	C.set(1, 0, 1.5);
	C.set(1, 1, 2.0);
	std::cout << "C:\n" << C << std::endl;

	A += B + C;	

	std::cout << "A:\n" << A << std::endl;
	std::cout << "B:\n" << B << std::endl;
	std::cout << "C:\n" << C << std::endl;
	
	//The following code provokes a crash

	Matrix D = Matrix();
	D = B*C;
	std::cout << "B*C:\n" << D << std::endl;

	Matrix E;
	E = B+C;
	std::cout << "B+C:\n" << E << std::endl;

	return 0;
}
