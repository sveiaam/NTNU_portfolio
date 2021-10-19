#pragma once
#include "Card.h"
#include <vector>

//4
class CardDeck {
private:
	std::vector<Card> cards = {}; //Vector with elements of class Card
	int currentCardIndex; //How many cards have been dealt?
	void swap(int a, int b); //Swaps the cards in positions a and b
public:
	CardDeck(); //Constructor
	void print(); //Prints the deck
	void printShort(); //Prints the deck in short-hand strings
	void shuffle(); //Shuffles the deck
	Card drawCard(); //Draws a card from the deck (returns Card type)
	/*Card operator [] (std::vector<Card> vec); //Operator definition*/
};
