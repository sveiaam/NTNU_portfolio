#pragma once
class Car
{
public:
	Car(int noOfFreeSeats);
	bool hasFreeSeats() const;
	void reserveFreeSeat();
private:
	int freeSeats;
};
