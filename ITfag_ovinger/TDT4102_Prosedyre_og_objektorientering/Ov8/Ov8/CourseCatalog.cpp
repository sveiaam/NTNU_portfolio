#include "CourseCatalog.h"
#include <iostream>
#include <map>
#include <utility>



CourseCatalog::CourseCatalog()
{
}


CourseCatalog::~CourseCatalog()
{
}


std::ostream &operator << (std::ostream &os, const CourseCatalog &c) {
	for (const auto &a : c.map) {
		os << a.first << ": " << a.second << std::endl;
	};
	return os;
}


void CourseCatalog::addCourse(std::string courseCode, std::string courseName) {
	map.insert({ courseCode, courseName });
}


void CourseCatalog::removeCourse(std::string courseCode) {
	map.erase(courseCode);
}


std::string CourseCatalog::getCourse(std::string courseCode) {
	return map[courseCode];
}


void CourseCatalog::addCourse2(std::string courseCode, std::string courseName) {
	map[courseCode] = courseName;
}


void testFunction() {
	CourseCatalog K;
	K.addCourse("TDT4102", "Prosedyre- og objektorientert programmering");
	K.addCourse("TFY4215", "Innføring i kvantefysikk");
	K.addCourse("TMA4320", "Introduksjon til vitenskapelige beregninger");
	K.addCourse("TMA4245", "Statistikk og sannsynlighet");
	K.addCourse("FY2450", "Astrofysikk");
	std::cout << K << std::endl;

	K.removeCourse("FY2450");
	std::cout << K << std::endl;

	std::cout << K.getCourse("TDT4102") << std::endl;
	std::cout << "\n";

	// Ingenting skjer
	K.addCourse("TDT4102", "C++");
	std::cout << K << std::endl;
	// Ting skjer ([]-operatoren overstyrer det som står der fra før, mens insert() ikke gjør det.)
	K.addCourse2("TDT4102", "C++");
	std::cout << K << std::endl;
}

