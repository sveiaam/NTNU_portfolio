#include "cannonball.h"
#include "utilities.h"
#include <iostream>
#include <ctime>

int main() {
	setlocale(LC_ALL, "Norwegian");
	std::srand(std::time(nullptr));
	playTargetPractice();
	return 0;
}
