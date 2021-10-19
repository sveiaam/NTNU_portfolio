#include "utilities.h"
#include <iostream>

const int SIZE = 4; //Antall tegn i koden
const int LETTERS = 6; //Antall muligheter per tegn
const int GUESSES = 10; //Antall forsøk spilleren har på å gjette riktig

int compareCharactersIndividually(char code[], char guess[], char letter) {
	int counter = 0;
	for (int i = 0; i < SIZE; i++) {
		if ((code[i] == letter) and (guess[i] == letter)) {
			counter += 1;
		};
	};
	return counter;
}
int checkCharactersAndPosition(char code[], char guess[]) {
	int counter = 0;
	for (int i = 0; i < LETTERS; i++) {
		counter += compareCharactersIndividually(code, guess, 'A' + i);
		};
	return counter;
};
int checkCharacters(char code[], char guess[]) {
	int counter = 0, numLet = 0;
	int occurencesCode[LETTERS] = {}, occurencesGuess[LETTERS] = {};
	fillOccurenceTable(occurencesCode, code, LETTERS, SIZE, 'A'); //Finner antall av hver bokstav i koden
	fillOccurenceTable(occurencesGuess, guess, LETTERS, SIZE, 'A'); //Finner antall av hver bokstav i gjetningen
	for (int i = 0; i < LETTERS; i++) {
		numLet = compareCharactersIndividually(code, guess, 'A' + i); //Antall av bokstav nr. i som er helt riktige
		if (occurencesGuess[i] > occurencesCode[i]) {
			occurencesGuess[i] = occurencesCode[i];
			counter += (occurencesGuess[i] - numLet);
		}
		else {
			counter += (occurencesGuess[i] - numLet);
		};
		numLet = 0;
	};
	return counter;
}

void playMastermind() {
	bool quit = false;
	while (not quit) {
		std::cout << "\n\nVI SPILLER MASTERMIND. DU HAR " << GUESSES << " FORSØK!\n\n\n";
		char code[SIZE + 1] = {};
		randomizeCString(code, SIZE + 1, 'A', 'A' + (LETTERS - 1)); //Genererer koden
		char guess[SIZE + 1] = {};
		int fullyCorrect = 0, partiallyCorrect = 0;
		int counter = 0;
		while (counter < GUESSES) {
			counter += 1;
			readInputToCString(guess, SIZE + 1, 'A', 'A' + (LETTERS - 1)); //Får inn spillerens gjetning
			fullyCorrect = checkCharactersAndPosition(code, guess); //Riktig bokstav og plassering
			partiallyCorrect = checkCharacters(code, guess); //Riktig bokstav, men feil plassering
			std::cout << "Runde " << counter << "  ||  Du gjetter: " << guess << std::endl;
			std::cout << "Fullstendig rette: " << fullyCorrect << "  ||  Delvis rette: " << partiallyCorrect << "\n\n";
			if (fullyCorrect == SIZE) {
				std::cout << "Du klarte det på " << counter << " forsøk!" << std::endl;
				break;
			};
		};
		if (counter > GUESSES) {
			std::cout << "Du tapte. Koden var: " << code << std::endl;
		};
		bool choiceMade = false;
		while (not choiceMade) {
			char choice = ' ';
			std::cout << "Vil du spille igjen? (y/n): ";
			std::cin >> choice;
			switch (choice) {
			case 'y':
				choiceMade = true;
				break;
			case 'n':
				quit = true;
				choiceMade = true;
				break;
			default:
				std::cout << ":::::::: UGYLDIG VALG ::::::::" << std::endl;
				break;
			};
		};
	};
}