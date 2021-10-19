#include "Rectangle.h"



Rectangle::Rectangle( const Color &c, const Line diagonal ) : Shape( c )
{
	this->botLeftX = diagonal.getX1();
	this->botLeftY = diagonal.getY1();

	this->botRightX = diagonal.getX2();
	this->botRightY = diagonal.getY1();

	this->topRightX = diagonal.getX2();
	this->topRightY = diagonal.getY2();

	this->topLeftX = diagonal.getX1();
	this->topLeftY = diagonal.getY2();
}


Rectangle::~Rectangle()
{
}

void Rectangle::draw( Image &im ) {
	Line bot = Line( this->getColor(),
		botLeftX, botLeftY, botRightX, botRightY );
	Line left = Line( this->getColor(),
		botLeftX, botLeftY, topLeftX, topLeftY );
	Line right = Line( this->getColor(),
		botRightX, botRightY, topRightX, topRightY );
	Line top = Line( this->getColor(),
		topLeftX, topLeftY, topRightX, topRightY );

	bot.draw( im );
	left.draw( im );
	right.draw( im );
	top.draw( im );
}