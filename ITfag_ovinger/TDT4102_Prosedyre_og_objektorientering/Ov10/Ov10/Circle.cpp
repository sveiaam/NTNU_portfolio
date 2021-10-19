#include "Circle.h"
#include <cmath>



Circle::Circle( const Color &c, const int radius, const int centerX, const int centerY ) : Shape(c)
{
	this->radius = radius;
	this->centerX = centerX;
	this->centerY = centerY;
}

Circle::~Circle()
{
}

void Circle::draw( Image &im ) {
	int x, y;
	for ( x = (int) -radius / std::sqrt( 2 ); x < (int) radius / std::sqrt( 2 ); x++ ) {
		y = (int) std::sqrt( std::pow( radius, 2 ) - std::pow( x, 2 ) );
		im.setPixelColor( centerX + x,
			centerY + y,
			this->getColor() );
		im.setPixelColor( centerX + x,
			centerY - y,
			this->getColor() );
	}
	for ( y = (int) -radius / std::sqrt( 2 ); y < (int) radius / std::sqrt( 2 ); y++ ) {
		x = (int) std::sqrt( std::pow( radius, 2 ) - std::pow( y, 2 ) );
		im.setPixelColor( centerX + x,
			centerY + y,
			this->getColor() );
		im.setPixelColor( centerX - x,
			centerY + y,
			this->getColor() );
	}
}

