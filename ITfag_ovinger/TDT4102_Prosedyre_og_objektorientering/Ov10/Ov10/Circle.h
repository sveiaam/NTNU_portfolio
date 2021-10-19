#pragma once
#include "Shape.h"
class Circle :
	public Shape
{
	int radius;
	int centerX;
	int centerY;

public:
	Circle( const Color &c, const int radius, const int centerX, const int centerY );
	~Circle();
	void draw( Image &im ) override;
};

