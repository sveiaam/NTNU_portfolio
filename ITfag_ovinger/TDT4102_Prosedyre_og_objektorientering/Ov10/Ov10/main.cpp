#include <iostream>
#include "Image.h"
#include "Matrix.h"
#include "Vector.h"
#include "Line.h"
#include "Rectangle.h"
#include "Circle.h"
#include "Canvas.h"

using namespace std;

int main(){
	/*
	Matrix A = Matrix(4, 1);
	std::cout << A << std::endl;
	A.set(0, 0, 1.0);
	A.set(1, 0, 2.0);
	A.set(2, 0, 3.0);
	A.set(3, 0, 4.0);
	std::cout << A << std::endl;
	
	Vector b = Vector(A);
	std::cout << b << std::endl;
	*/
	///////////////
	
	//Matrix A = Matrix(3, 3, 8);
	//Vector b = Vector(3);
	//b.set(0, 5);
	//b.set(1, 5);
	//b.set(2, 5);

	//std::cout << A << std::endl;
	//std::cout << b << std::endl;

	//std::cout << A * b << std::endl;
	
	

	
	Image P = Image( 100, 100 );
	Color a = Color( 0, 0, 255 );
	P.setPixelColor( 10, 10, a );

	Color b = P.getPixelColor( 10, 10 );
	
	std::cout << a.blue << " " << b.blue << std::endl;
	std::cout << a.green << " " << b.green << std::endl;
	std::cout << a.red << " " << b.red << std::endl;
	
	
	/*
	Image one = Image( 1920, 1080 );
	Color crayola_fuchsia = Color( 193, 84, 193 );
	one.fill( crayola_fuchsia );
	if ( saveImage( one, "oppg2h_1.BMP" ) == 0 ) {
		std::cout << "Image 1 : sucsess!" << std::endl;
	}
	else {
		std::cout << "Image 1 : Failure!" << std::endl;
	}

	Image two = Image( 1920, 1080 );
	two.fill( Color( 255, 255, 255 ) );
	two.setPixelColor( 10, 10, Color( 255, 0, 0 ) );
	if ( saveImage( two, "oppg2h_2.BMP" ) == 0 ) {
		std::cout << "Image 2 : sucsess!" << std::endl;
	}
	else {
		std::cout << "Image 2 : Failure!" << std::endl;
	}
	*/

	/*
	Image Q1 = Image( 200, 200 );
	Q1.fill( Color( 255, 255, 255 ) );
	if ( saveImage( Q1, "oppg4c_1.bmp" ) == 0 ) {
		std::cout << "oppg4c_1.bmp saved sucsessfully!" << std::endl;
	}
	else {
		std::cout << "oppg4c_1.mbp NOT saved!" << std::endl;
	}

	Line l1 = Line( Color( 255, 0, 0 ),
		0, 0,
		100, 50 );

	l1.draw( Q1 );
	if ( saveImage( Q1, "oppg4c_2.bmp" ) == 0 ) {
		std::cout << "oppg4c_2.bmp saved sucsessfully!" << std::endl;
	}
	else {
		std::cout << "oppg4c_2.bmp NOT saved!" << std::endl;
	}


	Image Q2 = Image( 200, 200 );
	Q2.fill( Color( 255, 255, 255 ) );
	if ( saveImage( Q2, "oppg4d_1.bmp" ) == 0 ) {
		std::cout << "oppg4d_1.bmp saved sucsessfully!" << std::endl;
	}
	else {
		std::cout << "oppg4d_1.bmp NOT saved!" << std::endl;
	}

	Line l2 = Line( Color( 255, 0, 0 ),
		0, 0,
		100, 200 );

	l2.draw( Q2 );

	if ( saveImage( Q2, "oppg4d_2.bmp" ) == 0 ) {
		std::cout << "oppg4d_2.bmp saved sucsessfully!" << std::endl;
	}
	else {
		std::cout << "oppg4d_2.bmp NOT saved!" << std::endl;
	}

	Image R = Image( 200, 200 );
	R.fill( Color( 255, 255, 255 ) );
	if ( saveImage( R, "oppg5b_1.bmp" ) == 0 ) {
		std::cout << "oppg5b_1.bmp saved sucsessfully!" << std::endl;
	}
	else {
		std::cout << "oppg5b_1.bmp NOT saved!" << std::endl;
	}

	Rectangle r = Rectangle( Color( 255, 0, 0 ), l1 );
	r.draw( R );
	
	if ( saveImage( R, "oppg5b_2.bmp" ) == 0 ) {
		std::cout << "oppg5b_2.bmp saved sucsessfully!" << std::endl;
	}
	else {
		std::cout << "oppg5b_2.bmp NOT saved!" << std::endl;
	}
	*/

	
	Image im = Image( 300, 300 );
	im.fill( Color(255, 255, 0) );
	Canvas canv;

	Circle head = Circle( Color(),
		100,
		150, 150 );
	Circle leftEye = Circle( Color(), 10, 110, 190 );
	Circle rightEye = Circle( Color(), 10, 190, 190 );
	
	Line mouth = Line( Color(),
		100, 100,
		200, 100 );
	
	canv.addShape( &head );
	canv.addShape( &leftEye );
	canv.addShape( &rightEye );
	canv.addShape( &mouth );

	canv.rasterizeTo( &im );

	if ( saveImage( im, "oppg6d.bmp" ) == 0 ) {
		std::cout << "oppg6d.bmp saved sucsessfully!" << std::endl;
	}
	else {
		std::cout << "oppg6d.mbp NOT saved!" << std::endl;
	}
	
	return 0;
}
