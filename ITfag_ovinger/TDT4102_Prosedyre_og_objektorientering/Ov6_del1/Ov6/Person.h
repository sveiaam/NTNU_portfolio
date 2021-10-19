#pragma once
#include <string>
#include <iostream>
#include <cctype>
#include "Car.h"

class Person
{
public:
	Person(std::string name, std::string email, Car *car); //Constructor w/ car

	//Begge er ok
	//Person(std::string name, std::string email) : name(name), email(email), car(nullptr) {}; //Constructor w/o car
	Person(std::string name, std::string email) : Person(name, email, nullptr) {};

	std::string getName() const;
	std::string getEmail() const;
	std::string setEmail();
	bool hasAvaliableSeats() const;
	friend std::ostream &operator << (std::ostream &os, const Person &p);
private:
	std::string name;
	std::string email;
	Car *car;
};



bool &operator < (const Person &p1, const Person &p2);
bool &operator == (const Person &p1, const Person &p2);