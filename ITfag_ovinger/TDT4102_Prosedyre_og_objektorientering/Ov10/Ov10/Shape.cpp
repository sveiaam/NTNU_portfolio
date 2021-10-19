#include "Shape.h"



Shape::Shape(const Color &c)
{
	col = c;
}


Shape::~Shape()
{
}


Color Shape::getColor() {
	return col;
}

