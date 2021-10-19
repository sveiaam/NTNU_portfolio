#pragma once
#include "Shape.h"
class Line :
	public Shape
{
	int startX, startY, endX, endY;

public:
	Line( const Color &c, int x1, int y1, int x2, int y2 );
	~Line();
	void draw(Image &im) override; //override sjekker om denne deklarasjonen kolliderer med parent-klassen(e)s deklarasjon av draw
	int getX1() const;
	int getX2() const;
	int getY1() const;
	int getY2() const;
};

