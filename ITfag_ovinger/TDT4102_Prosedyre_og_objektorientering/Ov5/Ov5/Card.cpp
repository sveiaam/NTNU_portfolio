#include "card.h"
//1
std::string suitToString(Suit suit) {
	std::string s;
	switch (suit) {
	case CLUBS:
		s = "clubs";
		break;
	case DIAMONDS:
		s = "diamonds";
		break;
	case HEARTS:
		s = "hearts";
		break;
	case SPADES:
		s = "spades";
		break;
	};
	return s;
}
std::string rankToString(Rank rank) {
	std::string s;
	switch (rank) {
	case TWO:
		s = "two";
		break;
	case THREE:
		s = "three";
		break;
	case FOUR:
		s = "four";
		break;
	case FIVE:
		s = "five";
		break;
	case SIX:
		s = "six";
		break;
	case SEVEN:
		s = "seven";
		break;
	case EIGHT:
		s = "eight";
		break;
	case NINE:
		s = "nine";
		break;
	case TEN:
		s = "ten";
		break;
	case JACK:
		s = "jack";
		break;
	case QUEEN:
		s = "queen";
		break;
	case KING:
		s = "king";
		break;
	case ACE:
		s = "ace";
		break;
	};
	return s;
}

//2
std::string toString(CardStruct card) {
	return rankToString(card.r) + " of " + suitToString(card.s);
	}
std::string toStringShort(CardStruct card) {
	std::string suitShort = suitToString(card.s).substr(0,1);
	int value = card.r;
	std::string rankShort = std::to_string(value);
	return suitShort + rankShort;
}

//3
void Card::initialize(Suit suit, Rank rank) {
	Card::suit = suit;
	Card::rank = rank;
	valid = true;
}
Suit Card::getSuit() {
	return Card::suit;
}
Rank Card::getRank() {
	return Card::rank;
}
std::string Card::toString() {
	if (valid == true) {
		return rankToString(getRank()) + " of " + suitToString(getSuit());
	}
	else {
		return "INVALID CARD";
	};
}
std::string Card::toStringShort() {
	std::string suitShort = suitToString(getSuit()).substr(0, 1);
	int rank = getRank();
	std::string rankShort = std::to_string(rank);
	if (valid == true) {
		return suitShort + rankShort;
	}
	else {
		return "INVALID CARD";
	};
}
Card::Card() {
	valid = false;
}
Card::Card(Suit suit, Rank rank){
	valid = true;
	Card::suit = suit;
	Card::rank = rank;
}
