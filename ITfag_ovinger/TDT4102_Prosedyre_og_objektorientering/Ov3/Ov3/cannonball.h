#pragma once
//1a
double acclY();
double acclX();
//1b
double velY(double initVelocityY, double time);
//1c
double posX(double initPositionX, double initVelocityX, double time);
double posY(double initPositionY, double initVelocityY, double time);
//1d
void printTime(double time);
//1e
double flightTime(double initVelocityY);

//4a
void getUserInput(double *theta, double *absVelocity);
double degToRad(double deg);
double getVelocityX(double theta, double absVelocity);
double getVelocityY(double theta, double absVelocity);
void getVelocityVector(double theta, double absVelocity, double *velocityX, double *velocityY);
//4b
double getDistanceTraveled(double velocityX, double velocityY);
//4c
double targetPractice(double distanceToTarget, double velocityX, double velocityY);

//6a
double calculateShot(double target);
void playTargetPractice();
