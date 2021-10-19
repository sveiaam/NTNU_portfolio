#pragma once
#include "CardDeck.h"

class Blackjack {
public:
	Blackjack(); //Constructor
	bool isAce(Card *card); //Returns true if input card has rank 14 (ace)
	int getCardValue(Card *card); //Returns the blackjack value of the input card (-1 for ace)
	int getPlayerCardValue(Card *card); //Returns the value of the card for the player
	int getDealerCardValue(Card *card, int remainingHandValue); //Returns the value of the card for the dealer
	bool askPlayerDrawCard(); //Returns true if player wants to draw a card
	void drawInitialCards(); //Deals initial hands and updates the hand values
	void playGame(); //Implements blackjack
private:
	CardDeck deck;
	int playerHand; //How many points is the player hand?
	int dealerHand; //How many points is the dealer hand?
	int playerCardsDrawn; //How many cards has the player drawn?
	int dealerCardsDrawn; //How many cards has the dealer drawn?
};
