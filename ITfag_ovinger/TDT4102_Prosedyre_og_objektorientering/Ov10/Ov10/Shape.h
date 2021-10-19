#pragma once
#include "Image.h"

class Shape
{
Color col;

public:
	Shape(const Color &c);
	~Shape();

	Color getColor();
	virtual void draw( Image &im ) = 0;
	//1) Pure virtual :: Ingen implementasjon
	//2) Vi kan ikke instansiere objekter av abstrakte klasser
};

