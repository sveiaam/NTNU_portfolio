#include "Image.h"

/*****************************************************
 * You _should_ change the functions in this file.   *
 * The following functions are provided so that      *
 * the code will compile, note however that the      *
 * program will not run before you have implemented  *
 * all the functions in this file.                   *
 *****************************************************/

Image::Image( int width, int height ) {
   /* Enter your code here */
}

Image::~Image()  {
   /* Enter your code here */
}

int Image::getWidth() const {
   /* Enter your code here */
   return 0;
}
int Image::getHeight() const  {
   /* Enter your code here */
   return 0;
}

const Pixel * Image::getScanLine(int line) const  {
   /* Enter your code here */
   return nullptr;
}
Pixel * Image::getScanLine(int line) {
   /* Enter your code here */
   return nullptr;
}

Color Image::getPixelColor( int x, int y ) const {
   /* Enter your code here */
   return Color();
}
void Image::setPixelColor( int x, int y, const Color &color ) {
   /* Enter your code here */
}

void Image::fill( const Color &color ) {
   /* Enter your code here */
}
