#include "Car.h"

Car::Car(int noOfFreeSeats) {
	freeSeats = noOfFreeSeats;
}

bool Car::hasFreeSeats() const {
	if (freeSeats > 0) {
		return true;
	}
	else {
		return false;
	};
}
void Car::reserveFreeSeat() {
	freeSeats -= 1;
}
