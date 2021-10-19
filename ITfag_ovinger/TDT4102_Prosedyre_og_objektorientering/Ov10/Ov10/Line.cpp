#include "Line.h"


Line::Line(const Color &c, int x1, int y1, int x2, int y2) : Shape(c)
{
	startX = x1;
	startY = y1;
	endX = x2;
	endY = y2;
}


Line::~Line()
{
}

void Line::draw( Image &im ) {
	int x = startX;
	int y = startY;
	double rise = (endY - startY) / (double) (endX - startX);
	if ( rise < 1 ) {
		while ( x < endX ) {
			y = (int) (endY - startY) / (double) (endX - startX) * (x - startX) + startY;
			im.setPixelColor( x,
				y,
				this->getColor() );
			x += 1;
		}
	}
	else {
		while ( y < endY ) {
			x = (int) (endX - startX) / (double) (endY - startY) * (y - startY) + startX;
			im.setPixelColor( x,
				y,
				this->getColor() );
			y += 1;
		}
	}
}

int Line::getX1() const{
	return startX;
}

int Line::getX2() const{
	return endX;
}

int Line::getY1() const{
	return startY;
}

int Line::getY2() const{
	return endY;
}
