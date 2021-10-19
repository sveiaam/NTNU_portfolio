#include <iostream>
#include "utilities.h"
#include <cmath>

//1
void testCallByValue() {
	int v0 = 5;
	int increment = 2;
	int iterations = 10;
	int result = incrementByValueNumTimes(v0, increment, iterations);
	std::cout << "v0: " << v0
		<< " increment: " << increment
		<< " iterations: " << iterations
		<< " result: " << result << std::endl;
}
void testCallByPointer() {
	int v0 = 5;
	int increment = 2;
	int iterations = 10;
	incrementByValuesNumTimes2(&v0, increment, iterations);
	std::cout << "v0: " << v0
		<< " increment: " << increment
		<< " iterations: " << iterations;
		//<< " result: " << result << std::endl;
}
void testSwap() {
	int a = 2, b = 3;
	std::cout << "a=" << a << ", b=" << b << ".\nForetar bytte...\n";
	swapNumbers(&a, &b);
	std::cout << "a=" << a << ", b=" << b << ".\n";
}

//2, 3
void testTableSorting() {
	int percentages[20] = {};
	std::cout << "20 elementer lang tabell med 0-elementer:\n";
	printArray(percentages, 20);
	randomizeArray(percentages, 20);
	std::cout << "Denne tabellen har nå tilfeldige prosentverdier (mellom 0 og 100):\n";
	printArray(percentages, 20);
	swapNumbers(&percentages[0], &percentages[1]);
	std::cout << "Nå byttes de to første elementene i tabellen:\n";
	printArray(percentages, 20);
	sortArray(percentages, 20);
	std::cout << "Nå sorteres tabellen (i stigende rekkefølge):\n";
	printArray(percentages, 20);
	std::cout << "Median: " << medianOfArray(percentages, 20) << std::endl;
}

//4
void testCStrings() {
	char grades[9] = {};
	randomizeCString(grades, 9, 'A', 'F');
	std::cout << "\nTilfeldig genererte karakterer fra 2 semestre (A-F): " << grades << std::endl;
	std::cout << "\nNå skal du taste inn 8 karakterer (fra 2 semestre).\n\n";
	readInputToCString(grades, 9, 'A', 'F');
	std::cout << "Du skrev inn karakterene: " << grades << std::endl;
	std::cout << "Antall A: " << countOccurencesOfCharacter(grades, 9, 'A') << std::endl;
	int gradeCount[6] = {};
	fillOccurenceTable(gradeCount, grades, 6, 9, 'A');
	std::cout << "Antall av hver karakter (A-F): ";
	for (int i = 0; i < 6; i++) {
		std::cout << gradeCount[i] << " ";
	};
	double avg = std::round((gradeAverage(gradeCount, 6)) * 10) / 10;
	std::cout << "\nKaraktergjennomsnitt: " << avg << std::endl;
	std::cout << "Gjennomsnittlig bokstavkarakter: " << static_cast<char>('A' + round(avg) - 1) << std::endl;

	char fiveYrGrades[41] = {};
	randomizeCString(fiveYrGrades, 41, 'A', 'E');
	std::cout << "\nTilfeldig genererte karakterer over 5 år (A-E):\n" << fiveYrGrades << std::endl;
	int fiveYrGradeCount[5] = {};
	fillOccurenceTable(fiveYrGradeCount, fiveYrGrades, 5, 41, 'A');
	std::cout << "Antall av hver karakter (A-E): ";
	for (int i = 0; i < 5; i++) {
		std::cout << fiveYrGradeCount[i] << " ";
	};
	double fiveYrAvg = std::round((gradeAverage(fiveYrGradeCount, 5)) * 10) / 10;
	std::cout << "\n5-årig karaktersnitt: " << fiveYrAvg << std::endl;
	std::cout << "Gjennomsnittlig bokstavkarakter: " << static_cast<char>('A' + round(fiveYrAvg) - 1) << std::endl;
}
