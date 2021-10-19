#pragma once
#include <map>
#include <string>

class CourseCatalog
{
public:
	CourseCatalog();
	~CourseCatalog();
	friend std::ostream &operator << (std::ostream &os, const CourseCatalog &c);
	void addCourse(std::string courseCode, std::string courseName);
	void removeCourse(std::string courseCode);
	std::string getCourse(std::string courseCode);

	void addCourse2(std::string courseCode, std::string courseName);
private:
	std::map<std::string, std::string> map;
};

void testFunction();
