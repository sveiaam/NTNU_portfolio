#pragma once
#include "Shape.h"
#include "Line.h"
class Rectangle :
	public Shape
{
	int botLeftX, botLeftY, botRightX, botRightY, topRightX, topRightY, topLeftX, topLeftY;

public:
	Rectangle( const Color &c, const Line diagonal );
	~Rectangle();
	void draw(Image &im) override;
};

