#include "utilities.h"
#include "tests.h"
#include "mastermind.h"
#include <iostream>

void runMenu() {
	bool quit = false;
	while (not quit) {
		std::cout << "\n::::::::::\n\nVelg hva du vil kjøre:\n\n" <<
			"(1) = testCallByValue\n" <<
			"(2) = testCallByPointer\n" <<
			"(3) = testSwap\n" <<
			"(4) = testTableSorting\n" <<
			"(5) = testCStrings\n" <<
			"(6) = playMastermind\n" <<
			"(q) = Avslutt programmet\n";
		char choice = ' ';
		std::cout << "Velg noe: ";
		std::cin >> choice;
		std::cout << "\n";
		switch (choice) {
		case 'q':
			quit = true;
			break;
		case '1':
			testCallByValue();
			break;
		case '2':
			testCallByPointer();
			break;
		case '3':
			testSwap();
			break;
		case '4':
			testTableSorting();
			break;
		case '5':
			testCStrings();
			break;
		case '6':
			playMastermind();
		default:
			std::cout << "\n:::::::: UGYLDIG VALG ::::::::\n" << std::endl;
		};
	};
}
