#include <vector>
#include "GameObjects.h"
#pragma once
int randomWithLimits(int maxLim, int minLim);

double acclY();
double acclX();

double velY(double initVelocityY, double time);

double posX(double initPositionX, double initVelocityX, double time);
double posY(double initPositionY, double initVelocityY, double time);

void printTime(double time);

double flightTime(double initVelocityY);

void getUserInput(double *theta, double *absVelocity);
double degToRad(double deg);
double getVelocityX(double theta, double absVelocity);
double getVelocityY(double theta, double absVelocity);
void getVelocityVector(double theta, double absVelocity, double *velocityX, double *velocityY);

double getDistanceTraveled(double velocityX, double velocityY);

double targetPractice(double distanceToTarget, double velocityX, double velocityY);

double calculateShot(double target);
void playTargetPractice();

//void removeVector(std::vector<Cannonball> vec);
