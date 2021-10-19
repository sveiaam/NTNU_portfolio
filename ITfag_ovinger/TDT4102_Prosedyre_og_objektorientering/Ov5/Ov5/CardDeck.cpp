#include "CardDeck.h"
#include "Card.h"
#include <iostream>
#include "utilites.h"

/*How many times we swap 2 cards in shuffle*/
const int SHUFFLESTEPS = 1000;

CardDeck::CardDeck() {
	/* Creates a vector with elements of type Card {class},
	initializes each element with different members of enum types Suit and Rank.
	Sets currentCardIndex to zero.*/
	currentCardIndex = 0;
	for (int i = CLUBS; i <= SPADES; i++) {
		for (int j = TWO; j <= ACE; j++) {
			cards.push_back(Card::Card(Suit(i), Rank(j)));
		};
	};
}
void CardDeck::swap(int a, int b) {
	std::swap(cards[a], cards[b]);
}
void CardDeck::print() {
	for (int i = 0; i < 52; i++) {
		Card currentCard = cards[i];
		std::string s =currentCard.toString();
		std::cout << s << " ";
	};
}
void CardDeck::printShort() {
	for (int i = 0; i < 52; i++) {
		Card currentCard = cards[i];
		std::string s = currentCard.toStringShort();
		std::cout << s << " ";
	};
}
void CardDeck::shuffle() {
	for (int i = 0; i < SHUFFLESTEPS; i++) {
		/*Randomly choose which cards to swap*/
		int a = randomWithLimits(0, 51);
		int b = randomWithLimits(0, 51);
		/*Swap the cards*/
		CardDeck::swap(a, b);
	};
}
Card CardDeck::drawCard() {
	Card currentCard = cards[currentCardIndex];
	currentCardIndex += 1;
	return currentCard;
}