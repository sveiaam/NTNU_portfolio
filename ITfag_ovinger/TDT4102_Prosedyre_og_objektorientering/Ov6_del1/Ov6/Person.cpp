#include "Person.h"

Person::Person(std::string name, std::string email, Car *car) {
	Person::name = name;
	Person::email = email;
	Person::car = car;
}

std::string Person::getEmail() const {
	return email;
}
std::string Person::getName() const {
	return name;
}
std::string Person::setEmail() {
	std::string a;
	std::cout << "Skriv inn email: ";
	std::cin >> a;
	return a;
}
bool Person::hasAvaliableSeats() const {
	if (car == nullptr) {
		return false;
	}
	else {
		return car->hasFreeSeats();
	};
}

std::ostream &operator << (std::ostream &os, const Person &p) {
	std::string s;
	if (p.hasAvaliableSeats()) {
		s = "yes";
	}
	else {
		s = "no";
	};
	os << "name: " << p.getName() << ". email: " << p.getEmail() << ". free seats: " << s << ".";
	//os << "name: " << p.getName() << ". email: " << p.getEmail();
	return os;
}

bool &operator < (const Person &p1, const Person &p2) {
	/*Obtain names*/
	std::string name1 = p1.getName();
	std::string name2 = p2.getName();
	/*Obtain the shortest name*/
	int shortestStringNr;
	int shortestStringLenght;
	if (name1.size() < name2.size()) {
		shortestStringNr = 1;
		shortestStringLenght = name1.size();
	}
	else if (name1.size() > name2.size()) {
		shortestStringNr = 2;
		shortestStringLenght = name2.size();
	}
	else {
		shortestStringNr = 0;
		shortestStringLenght = name1.size();
	};
	/*Compare letter by letter*/
	bool truthValue;
	int i = 0;
	char currentLetter1;
	char currentLetter2;
	while (i < shortestStringLenght) {
		currentLetter1 = std::toupper(name1[i]);
		currentLetter2 = std::toupper(name2[i]);
		if (currentLetter1 < currentLetter2) {
			//truthValue = true;
			truthValue = false;
			break;
		}
		else if (currentLetter1 > currentLetter2) {
			//truthValue = false;
			truthValue = true;
			break;
		}
		else {
			i++;
		};
	};
	if (i == shortestStringLenght) {
		//If p2 has the shortest name
		if (shortestStringNr == 2) {
			truthValue = false;
			//truthValue = true;
		}
		else {
			truthValue = true;
			//truthValue = false;
		};
	};
	return truthValue;
}
bool &operator == (const Person &p1, const Person &p2) {
	bool truthValue;
	if ((p1 < p2) or (p2 < p1)) {
		truthValue = false;
	}
	else {
		truthValue = true;
	};
	return truthValue;
}
