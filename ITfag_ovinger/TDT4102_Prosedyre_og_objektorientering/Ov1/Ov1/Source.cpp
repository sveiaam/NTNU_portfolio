//TDT4102 - �ving 1 - Svein �mdal

#include <iostream>;

//Oppg a
int max(int a, int b) {
	if (a > b) { std::cout << "A is greater than B" << std::endl; return a; }
	else { std::cout << "B is greater than or equal A" << std::endl; return b; };
}

//Oppg c
//Ved innsetting av n, printer funksjonen (ogs� i python) Fibonacci-tall nummer n+1 til slutt, og ikke nummer n.
int fibonacci(int n) {
	int a = 0;
	int b = 1;
	std::cout << "Fibonacci numbers:" << std::endl;
	for (int x = 1; x < n + 1; x++) {
		std::cout << x << "," << b << std::endl;
		int temp = b;
		b += a;
		a = temp;
	};
	std::cout << "----" << std::endl;
	return b;
}

//Oppg d
int squareNumberSum(int n) {
	int totalSum = 0;
	for (int i = 1; i < n; i++) {
		totalSum += i * i;
		std::cout << i * i << std::endl;
	};
	std::cout << totalSum << std::endl;
	return totalSum;
}

//Oppg e
int triangleNumbersBelow(int n) {
	int acc = 1;
	int num = 2;
	std::cout << "Triangle numbers below " << n << ":" << std::endl;
	while (acc < n) {
		std::cout << acc << std::endl;
		acc += num;
		num += 1;
	}
	std::cout << "" << std::endl;
	return 0;
}

bool isTriangleNumber(int number) {
	int acc = 1;
	while (number > 0) {
		number -= acc;
		acc += 1;
	};
	return number == 0;
}

//Oppg f
bool isPrime(int n) {
	bool primeness = 1;
	if (n < 2) { return 0; };	//Legger til dette for � hindre at 1, 0, og negative tall oppfattes som primtall
	for (int j = 2; j < n; j++) {
		if (n%j == 0) { primeness = 0; break;}
	};
	return primeness;
}

//Oppg g
int naivePrimeNumberSearch(int n) {
	for (int number = 2; number < n; number++) {
		if (isPrime(number)) { std::cout << number << " is a prime" << std::endl; };
	};
	return 0;
}

//Oppg h
int findGreatestDivisor(int n) {
	for (int divisor = n - 1; divisor > 0; divisor = divisor - 1) {
		if (n%divisor == 0) { return divisor; };
	};
}

//Inkluderer main for � teste de andre funksjonene.
int main() {
	std::cout << "\n ** Oppgave a)" << std::endl;
	std::cout << max(5,6) << std::endl;
	std::cout << "\n ** Oppgave c)" << std::endl;
	std::cout << fibonacci(12) << std::endl;
	std::cout << "\n ** Oppgave d)" << std::endl;
	squareNumberSum(6);
	std::cout << "\n ** Oppgave e)" << std::endl;
	triangleNumbersBelow(11);
	if (isTriangleNumber(6)) {std::cout << "True" << std::endl; }
	else { std::cout << "False" << std::endl; };
	std::cout << "\n ** Oppgave f)" << std::endl;
	if (isPrime(101)) { std::cout << "True" << std::endl; }
	else { std::cout << "False" << std::endl; };
	std::cout << "\n ** Oppgave g)" << std::endl;
	naivePrimeNumberSearch(200);
	std::cout << "\n ** Oppgave h)" << std::endl;
	std::cout << "Largest divisor of " << 27 << " is " << findGreatestDivisor(27) << std::endl;
	return 0;
}
