#include "GameObjects.h"
#include "utilities.h"
#include <cmath>

// implement all (member) functions in this file

bool hitTarget(const Cannonball& c, const Target& t) {
	return c.shape.getGlobalBounds().intersects(t.shape.getGlobalBounds());
}

bool Cannonball::hasLanded() const {
	return getPosY() + size < 0;
}

double Cannonball::getAirTime() const {
	return SPEED_FACTOR * clock.getElapsedTime().asSeconds();
}

double Cannon::getTipX() const {
	return length * std::cos(degToRad(theta));
}

double Cannon::getTipY() const {
	return length * std::sin(degToRad(theta));
}


/*My function inplementations::*/

Target::Target(double size, double position) {
	Target::size = size;
	Target::position = position;
	shape = sf::RectangleShape(sf::Vector2f(size, size));
	shape.setFillColor(sf::Color(255, 0, 0));
	shape.setPosition(position, 0);
}
void Target::update() {//Intentionally does nothing
}
void Target::draw(sf::RenderWindow& window) {
	window.draw(shape);
}


Cannon::Cannon() {
	shape.setSize(sf::Vector2f(width, length)); //Give shape
	shape.setFillColor(sf::Color(255, 150, 0)); //Give color
	shape.setOrigin(width / 2, 0); //Give origin
	shape.setPosition(0, 0); //Give position
}
void Cannon::update() {
	shape.setRotation(theta-90); //In degrees
}
void Cannon::draw(sf::RenderWindow& window) {
	window.draw(shape);
}
void Cannon::incrementAngle(double dtheta) {
	theta += dtheta;
}
void Cannon::decrementAngle(double dtheta) {
	theta -= dtheta;
}
void Cannon::incrementVelocity(double dvel) {
	velocity += dvel;
}
void Cannon::decrementVelocity(double dvel) {
	velocity -= dvel;
}

Cannonball Cannon::shoot() {
	double startPosX = getTipX();
	double startPosY = getTipY();
	Cannonball ball = Cannonball(theta, velocity, startPosX, startPosY);
	return ball;
}


Cannonball::Cannonball(double angle, double initial_velocity, double startPosX, double startPosY) {
	Cannonball::startPosX = startPosX;
	Cannonball::startPosY = startPosY;
	startVelX = initial_velocity * std::cos(degToRad(angle));
	startVelY = initial_velocity * std::sin(degToRad(angle));
	shape.setRadius(size);
	shape.setOrigin(size, size);
	shape.setFillColor(sf::Color(255, 150, 0));
	clock.restart();
}
double Cannonball::getPosX() const {
	double time = getAirTime();
	return posX(startPosX, startVelX, time);
}
double Cannonball::getPosY() const {
	double time = getAirTime();
	return posY(startPosY, startVelY, time);
}
void Cannonball::update() {
	shape.setPosition(getPosX(), getPosY());
}
void Cannonball::draw(sf::RenderWindow& window) {
	window.draw(shape);
}

