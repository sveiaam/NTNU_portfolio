#include "Oppg1.h"
#include <iostream>

void fillInFibonacciNumbers(int result[], int length) {
	/* Assume result[] is of lenght length. */

	int iter = 0;
	int currentFib = 1;
	int previousFib = 0;

	while (iter < length) {
		result[iter] = currentFib;
		currentFib += previousFib;
		previousFib = result[iter];
		iter += 1;
	};
};

void printArray(int arr[], int lenght) {
	for (int i = 0; i < lenght; i++) {
		std::cout << arr[i] << "  ";
	};
	std::cout << "\n\n";
}

void createFibonacci() {
	int length;
	std::cout << "Length of Fibonacci sequence: ";
	std::cin >> length;

	/* Create dynamic table: */
	int *table = new int[length];
	/* Insert Fibonacci numbers into table: */
	fillInFibonacciNumbers(table, length);
	/* Print the table: */
	printArray(table, length);
	/* Release memory: */
	delete[] table;
	table = nullptr;
};
