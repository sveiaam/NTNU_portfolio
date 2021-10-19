#include "Person.h"

void personTests();

int main() {
	setlocale(LC_ALL, "Norwegian");
	personTests();
	return 0;
}

void personTests() {
	Car car1 = Car(2);
	Car car2 = Car(0);
	Person pers1 = Person("Solberg, Erna", "erna@statsminister.no", &car1);
	Person pers2 = Person("Solberg, Petter", "petter@subaru.com", &car2);
	Person pers3 = Person("Natvig, Lasse", "lasse.natvig@ntnu.no");
	std::cout << "pers1:: " << pers1 << std::endl;
	std::cout << "pers2:: " << pers2 << std::endl;
	std::cout << "pers3:: " << pers3 << std::endl;
	if (pers2 < pers1) {
		std::cout << pers1.getName() << " kommer før " << pers2.getName() << " i alfabetet." << std::endl;
	}
	else {
		std::cout << pers1.getName() << " kommer ikke før " << pers2.getName() << " i alfabetet." << std::endl;
	};
}
