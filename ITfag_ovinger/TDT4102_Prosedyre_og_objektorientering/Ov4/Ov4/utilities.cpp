#include <iostream>
#include <cctype>

//1
int incrementByValueNumTimes(int startValue, int increment, int numTimes) {
	for (int i = 0; i < numTimes; i++) {
		startValue += increment;
	}
	return startValue;
}
void incrementByValuesNumTimes2(int *startValue, int increment, int numTimes) {
	int a = 0;
	for (int i = 0; i < numTimes; i++) {
		a += increment;
	};
	*startValue += a;
}
void swapNumbers(int *a, int *b) {
	int temp = *a;
	*a = *b;
	*b = temp;
}

//2
void printArray(int table[], int n) {
	for (int i = 0; i < n; i++) {
		std::cout << table[i] << " ";
	};
	std::cout << std::endl;
}
int randomWithLimits(int minLim, int maxLim) {
	int diff = maxLim - minLim;
	int num = std::rand() % (diff + 1) + minLim;
	return num;
}
void randomizeArray(int table[], int n) {
	for (int i = 0; i < n; i++) {
		table[i] = randomWithLimits(0, 100);
	};
}

//3
void sortArray(int table[], int n) { //Bubble sort
	for (int i = 0; i < n - 1; i++) {
		for (int j = 0; j < n - 1 - i; j++) {
			if (table[j] > table[j + 1]) {
				swapNumbers(&table[j], &table[j + 1]);
			};
		};
	};
}
double medianOfArray(int sortedTable[], int n) {
	bool odd = false;
	if (n % 2 == 1) {
		odd = true;
	};
	if (odd) {
		int k = (n - 1) / 2;
		return sortedTable[k];
	}
	else {
		int k = n / 2;
		return static_cast<double> (sortedTable[k]+sortedTable[k-1])/2;
	};
}

//4
void randomizeCString(char table[], int n, char lowerLim, char upperLim) {
	for (int i = 0; i < n-1; i++) {
		table[i] = randomWithLimits(lowerLim, upperLim);
	};
}
void readInputToCString(char table[], int n, char lowerLim, char upperLim) {
	char ch = '\0', CH = '\0';
	for (int i = 0; i < n - 1; i++) {
		do {
			std::cout << "Skriv inn tegn mellom " << lowerLim << " og " << upperLim << std::endl;
			std::cout << "Tegn: ";
			std::cin >> ch;
			CH = toupper(ch);
		} while ((CH < lowerLim) or (upperLim < CH));
		std::cout << CH << " registrert.\n\n";
		table[i] = CH;
	};
}
int countOccurencesOfCharacter(char table[], int n, char target) {
	int counter = 0;
	for (int i = 0; i < n; i++) {
		if (table[i] == target) {
			counter += 1;
		};
	};
	return counter;
}
//Hjelpefunksjoner for 4h og 4i
void fillOccurenceTable(int occurences[], char table[], int lenOcc, int lenTable, char firstValue) {
	int a = 0;
	for (int i = 0; i < lenOcc; i++) {
		char c = firstValue + i;
		a = countOccurencesOfCharacter(table, lenTable, c);
		occurences[i] = a;
	};
}
double gradeAverage(int table[], int n) {
	int counter = 0;
	for (int i = 0; i < n; i++) { //Teller opp totalt # karakterer
		counter += table[i];
	};
	double value = 0;
	for (int i = 0; i < n; i++) { //Legger sammen vektede antall karakterer
		value += table[i] * (i + 1);
	};
	return value / counter;
}
