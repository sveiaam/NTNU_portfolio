#pragma once
#include <string>
//1
enum Suit { CLUBS, DIAMONDS, HEARTS, SPADES };
enum Rank { TWO = 2, THREE = 3, FOUR = 4, FIVE = 5, SIX = 6, SEVEN = 7, EIGHT = 8, NINE = 9, TEN = 10, JACK = 11, QUEEN = 12, KING = 13, ACE = 14 };
/*Returns string of a value in enum Suit*/
std::string suitToString(Suit suit);
/*Returns string of a value in enum Rank*/
std::string rankToString(Rank rank);

//2
struct CardStruct {
	Suit s;
	Rank r;
};
/*Returns string of a card - i.e. "Rank of Suit"*/
std::string toString(CardStruct card);
/*Returns string; shortened card - i.e. "S R"*/
std::string toStringShort(CardStruct card);

//3
class Card {
private:
	Suit suit;
	Rank rank;
	bool valid;
public:
	void initialize(Suit suit, Rank rank); //Does the same as constructor
	Suit getSuit(); //Retrieve Suit
	Rank getRank(); //Retrieve Rank
	std::string toString(); //Retrieve string describing card
	std::string toStringShort(); //Retrieve short-hand string describing card
	Card();	//Constructor
	Card(Suit suit, Rank rank); //Constructor
};
