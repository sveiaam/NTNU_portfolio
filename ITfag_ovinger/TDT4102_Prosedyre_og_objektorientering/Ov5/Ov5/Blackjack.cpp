#include "Blackjack.h"
#include <iostream>

Blackjack::Blackjack() {
	playGame();
}

bool Blackjack::isAce(Card *card) {
	if (card->getRank() == 14) {
		return true;
	}
	else {
		return false;
	};
}
int Blackjack::getCardValue(Card *card) {
	if (isAce(card)) {
		return -1;
	}
	else if (card->getRank() > 10) {
		return 10;
	}
	else {
		return card->getRank();
	};
}
int Blackjack::getPlayerCardValue(Card *card) {
	int val = getCardValue(card);
	if (val != -1) {
		return val;
	}
	else {
		bool valid = false;
		char ch = '\0', CH = '\0';
		do {
			std::cout << "Value of ace ((a for 1) and (b for 11)): ";
			std::cin >> ch;
			CH = toupper(ch);
			if ((CH == 'A') or (CH == 'B')) {
				valid = true;
			}
			else {
				std::cout << "\nInvalid choice\n\n";
			};
		} while (not valid);
		if (CH == 'A') {
			return 1;
		}
		else {
			return 11;
		};
	};
}
int Blackjack::getDealerCardValue(Card *card, int remainingHandValue) {
	int val = getCardValue(card);
	if (val != -1) {
		return val;
	}
	else {
		if (remainingHandValue + 11 <= 21) {
			return 11;
		}
		else {
			return 1;
		};
	};
}
bool Blackjack::askPlayerDrawCard() {
	bool valid = false;
	char ch = '\0', CH = '\0';
	do {
		std::cout << "Draw another card? (y/n) :: ";
		std::cin >> ch;
		CH = toupper(ch);
		if ((CH == 'Y') or (CH == 'N')) {
			valid = true;
		}
		else {
			std::cout << "\nInvalid choice\n\n";
		};
	} while (valid == false);
	if (CH == 'Y') {
		std::cout << "\n::: Drawing a card:::\n";
		return true;
	}
	else {
		return false;
	};
}
void Blackjack::drawInitialCards() {
	/*Initialize*/
	playerHand = 0;
	dealerHand = 0;
	/*Set up the players initial hand*/
	Card playersCard = deck.drawCard();
	std::cout << "Player's first card is " << playersCard.toString() << std::endl;
	playerHand += getPlayerCardValue(&playersCard);
	playersCard = deck.drawCard();
	std::cout << "Player's second card is " << playersCard.toString() << std::endl;
	playerHand += getPlayerCardValue(&playersCard);
	/*Set up the dealers initial hand*/
	Card dealersCard = deck.drawCard();
	dealerHand += getDealerCardValue(&dealersCard, dealerHand);
	std::cout << "Dealer's first card is " << dealersCard.toString() << "\n\n";
	dealersCard = deck.drawCard();
	dealerHand += getDealerCardValue(&dealersCard, dealerHand);
	/*Update cards drawn*/
	playerCardsDrawn = 2;
	dealerCardsDrawn = 2;
}
void Blackjack::playGame() {
	/*Initialize game*/
	std::cout << "#################\nPLAYING BLACKJACK\n#################\n\n";
	deck.shuffle();
	bool victory = false;
	bool playerBlackjack = false;
	bool dealerBlackjack = false;
	bool playerChoosing = true;
	drawInitialCards();

	/*Check for blackjack*/
	if (playerHand == 21) {
		playerBlackjack = true;
	};
	if (dealerHand == 21) {
		dealerBlackjack = true;
	};

	/*Let the player complete their hand*/
	while (playerChoosing) {
		Card currentCard;
		std::cout << "Your hand has value: " << playerHand << "\n\n";
		playerChoosing = askPlayerDrawCard();
		if (playerChoosing) {
			currentCard = deck.drawCard();
			std::cout << "You drew: " << currentCard.toString() << "\n\n";
			playerHand += getPlayerCardValue(&currentCard);
			playerCardsDrawn += 1;
		}
		else {
			break;
		};
		if (playerHand > 21) {
			playerBlackjack = false;
			break;
		};
	};

	/*Let the dealer complete their hand*/
	Card currentCard;
	while (dealerHand < 17) {
		currentCard = deck.drawCard();
		dealerHand += getDealerCardValue(&currentCard, dealerHand);
		dealerCardsDrawn += 1;
	};
	if ((dealerHand > 21) and not (playerHand > 21)) {
		victory = true;
	}

	/*Compare the hands*/
	if (((playerBlackjack and dealerBlackjack) or (not playerBlackjack and not dealerBlackjack)) and not (playerHand > 21)) {
		if (playerHand > dealerHand) {
			victory = true;
		};
	}
	else {
		if (playerBlackjack) {
			victory = true;
		};
	};

	/*Check for victory and celebrate/regret*/
	if (victory) {
		std::cout << "\n\n########   You won!   ########\n\n\n";
		std::cout << "Your hand value: " << playerHand << " with " << playerCardsDrawn << " cards drawn. Dealer's hand value: " << dealerHand << " with " << dealerCardsDrawn << " cards drawn.\n\n";
	}
	else {
		std::cout << "\n\n########   You lost!   ########\n\n\n";
		std::cout << "Your hand value: " << playerHand << " with " << playerCardsDrawn << " cards drawn. Dealer's hand value: " << dealerHand << " with " << dealerCardsDrawn << " cards drawn.\n\n";
	};
}
