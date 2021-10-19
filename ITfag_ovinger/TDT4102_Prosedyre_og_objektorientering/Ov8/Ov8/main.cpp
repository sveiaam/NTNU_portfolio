#include "file_management.h"
#include "CourseCatalog.h"
#include <iostream>


int main() {
	setlocale(LC_ALL, "Norwegian");
	//writeToFile();
	//readFromFile("oppg1.txt", "oppg1_linenrs.txt");
	//characterStatistics("oppg1.txt");
	//characterStatistics("The_Idiot_Dostoyevsky.txt");  // This one mysteriously fails
	//testFunction();
	wordStatistics("The_Idiot_Dostoyevsky.txt");
	//wordStatistics("oppg4.txt");
	return 0;
}