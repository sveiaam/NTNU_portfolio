#pragma once
#include <vector>
#include "Shape.h"
#include "Line.h"
#include "Rectangle.h"


class Canvas
{
	std::vector<Shape*> shapes;
public:
	Canvas();
	~Canvas();
	void addShape( Shape *newshape );
	void rasterizeTo(Image *im);

};

