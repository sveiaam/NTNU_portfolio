#include "utilities.h"
#include <cstdlib>
#include <ctime>
#include <cmath>
#include <iostream>

const double pi = 3.14159265359;

int randomWithLimits(int minLim, int maxLim) {
	int diff = maxLim - minLim;
	int num = std::rand() % (diff + 1) + minLim;
	return num;
}

double acclY() {
	return -9.81;
}
double acclX() {
	return 0;
}

double velY(double initVelocityY, double time) {
	return initVelocityY + acclY() * time;
}

double posX(double initPositionX, double initVelocityX, double time) {
	return initPositionX + initVelocityX * time + 0.5 * acclX() * std::pow(time, 2.0);
}
double posY(double initPositionY, double initVelocityY, double time) {
	return initPositionY + initVelocityY * time + 0.5 * acclY() * std::pow(time, 2.0);
}

void printTime(double time) {
	int hours = static_cast<int> (time) / 3600;
	time -= hours * 3600;
	int minutes = static_cast<int> (time) / 60;
	time -= minutes * 60;
	double seconds = time;
	std::cout << "time is " << hours << " hours, " << minutes << " minutes, and " << seconds << " seconds." << std::endl;
}

double flightTime(double initVelocityY) {
	return -2 * initVelocityY / acclY();
}

void getUserInput(double *theta, double *absVelocity) {
	std::cout << "Skriv inn vinkel fra x-aksen (i grader): ";
	std::cin >> *theta;
	double absVel = -1.0;
	do {
		std::cout << "Skriv inn startfart (absoluttverdi): ";
		std::cin >> absVel;
	} while (absVel < 0);
	*absVelocity = absVel;
}
double degToRad(double deg) {
	if (deg >= 0) {
		while (deg > 180.0) {
			deg -= 360.0;
		};
	}
	else {
		while (deg < -180.0);
		deg += 360.0;
	};
	return (pi*deg) / 180.0;
}
double getVelocityX(double theta, double absVelocity) {
	return absVelocity * std::cos(theta);
}
double getVelocityY(double theta, double absVelocity) {
	return absVelocity * std::sin(theta);
}
void getVelocityVector(double theta, double absVelocity, double *velocityX, double *velocityY) {
	*velocityX = getVelocityX(theta, absVelocity);
	*velocityY = getVelocityY(theta, absVelocity);
}

double getDistanceTraveled(double velocityX, double velocityY) {
	double time = flightTime(velocityY);
	double dist = posX(0, velocityX, time);
	return dist;
}

double targetPractice(double distanceToTarget, double velocityX, double velocityY) {
	return getDistanceTraveled(velocityX, velocityY) - distanceToTarget;
}

double calculateShot(double target) {
	double theta, absVelocity;
	getUserInput(&theta, &absVelocity);
	theta = degToRad(theta);
	double velocityX = getVelocityX(theta, absVelocity), velocityY = getVelocityY(theta, absVelocity);
	return targetPractice(target, velocityX, velocityY);
}
void playTargetPractice() {
	std::cout << "Skyt med kanon mot et tilfeldig generert mål mellom 100 og 1000 meter unna!\n\n###\n";
	int target = randomWithLimits(100, 1000);
	int counter = 0;
	while (counter < 10) {
		counter += 1;
		std::cout << "\nForsøk nr. " << counter << ":" << std::endl;
		double diff = calculateShot(target);
		if (std::abs(diff) <= 5.0) {
			std::cout << "\nGratulerer! Du traff blinken på " << counter << " forsøk!" << std::endl;
			std::cout << "Målet var " << target << " meter unna kanonen." << std::endl;
			break;
		}
		else if (diff < 0) {
			std::cout << "Du skjøt for kort. Avstanden er " << std::abs(diff) << " meter." << std::endl;
		}
		else {
			std::cout << "Du skjøt for langt. Avstanden er " << diff << " meter." << std::endl;
		};
	};
	if (counter >= 10) {
		std::cout << "\nDu har tapt spillet. Målet var " << target << " meter unna kanonen." << std::endl;
	};
}

/*
void removeVector(std::vector<Cannonball> vec) {
	while (vec.size() > 0) {
		vec.erase(0);
	}
}
*/
