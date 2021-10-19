#include "Image.h"

/*****************************************************
 * You _should_ change the functions in this file.   *
 * The following functions are provided so that      *
 * the code will compile, note however that the      *
 * program will not run before you have implemented  *
 * all the functions in this file.                   *
 *****************************************************/

Image::Image( int width, int height) {
	data = new Pixel[width*height] { Color() };
	this->height = height;
	this->width = width;
}

Image::~Image()  {
	delete[] data;
	data = nullptr;
}

int Image::getWidth() const {
	return width;
}
int Image::getHeight() const  {
	return height;
}
// const etter getWidth og getHeight sikrer at funksjonene ikke kan endre på medlemsvariablene hhv width og height.

const Pixel * Image::getScanLine(int line) const  {
	// Antar at line = 0 betyr første (indeks 0) rad av bildet
	return &data[ width*line ];
}
Pixel * Image::getScanLine(int line) {
	// Antar at line = 0 betyr første (indeks 0) rad av bildet
	return &data[ width*line ];
}

Color Image::getPixelColor( int x, int y ) const {
	// Only fetch pixels on the grid
	if ( (x < width) && (y < height) && (x > 0) && (y > 0) ) {
		return data[ width*y + x ];
	}
	// If not on grid, return uninitialized color
	else {
		return Color();
	}

}
void Image::setPixelColor( int x, int y, const Color &color ) {
	// Only change pixels on the grid
	if ( (x < width) && (y < height) && (x > 0) && (y > 0) ) {
		data[ width*y + x ] = color;
	}
}

void Image::fill( const Color &color ) {
	for ( int i = 0; i < width*height; i++ ) {
		data[ i ] = color;
	}
}
