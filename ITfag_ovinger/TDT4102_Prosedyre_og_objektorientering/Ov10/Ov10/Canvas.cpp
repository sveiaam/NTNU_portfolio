#include "Canvas.h"



Canvas::Canvas()
{
}


Canvas::~Canvas()
{
}


void Canvas::addShape( Shape *newshape ) {
	shapes.push_back( newshape );
}

void Canvas::rasterizeTo(Image *im) {
	for ( Shape *it : shapes ) {
		it->draw( *im );
	}
}
