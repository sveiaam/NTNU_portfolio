#include <iostream>
#include "switchmenu.h"
#include <ctime>

//1a
/*
incrementByValueNumTimes tar inn a, b og n, og returnerer a + bn.
testCallByValue setter inn a = 5, b = 2 og n = 10, vil derfor få ut 5 + 2*10 = 25 fra funksjonen.
testCallByValue vil så printe alle disse verdiene (5, 2, 10 og 25)
*/

int main() {
	setlocale(LC_ALL, "Norwegian");
	std::srand(std::time(nullptr));
	runMenu();
}
