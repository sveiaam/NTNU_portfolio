#include <SFML/Graphics.hpp>
#include <SFML/Window.hpp>
#include <algorithm>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <iostream>
#include <vector>

#include "GameObjects.h"
#include "utilities.h"

int main() {
	std::srand(std::time(nullptr));
	rand();

	// window size
	const double WIN_HEIGHT = 600;
	const double WIN_WIDTH = 1200;

	// create a window
	sf::ContextSettings settings;
	settings.antialiasingLevel = 8; // "smoother" edges - not necessary
	sf::RenderWindow window(sf::VideoMode(WIN_WIDTH, WIN_HEIGHT), "TargetPractice", sf::Style::Close, settings);
	window.setFramerateLimit(30);

	// flip coordinates to make (0, 0) in lower left corner
	// in order to simplify simulation
	sf::View view(window.getView());
	view.setSize(WIN_WIDTH, -WIN_HEIGHT);
	window.setView(view);

	// start the clock
	sf::Clock clock;

	// variable indicating if the player has hit the target
	bool gameOver = false;

	// create game objects here ****
	int randInt = randomWithLimits(0, 1180);
	// std::cout << randInt;

	Target target = Target(20, randInt);
	Cannon cannon = Cannon();
	std::vector<Cannonball> allCannonballs;

	// main loop
	while (window.isOpen()) {
		sf::Event event;
		// while there are still unhandled events
		while (window.pollEvent(event)) {
			switch (event.type) {
			case sf::Event::Closed:
				window.close();
				break;
			case sf::Event::KeyPressed:
				switch (event.key.code) {
				case sf::Keyboard::Escape:
				case sf::Keyboard::Q:
					window.close();
					break;
				default:
					break;
				}
				// all events that only should be handled
				// while the game is not over, should
				// be placed here inside this if
				// (ex: moving the cannon, shooting)
				if (!gameOver) {
					switch (event.key.code) {
						// add case for new keyboard events here!
					case sf::Keyboard::Up:
						cannon.incrementVelocity();
						break;
					case sf::Keyboard::Down:
						cannon.decrementVelocity();
						break;
					case sf::Keyboard::Left:
						cannon.incrementAngle();
						break;
					case sf::Keyboard::Right:
						cannon.decrementAngle();
						break;
					case sf::Keyboard::Space: {
						Cannonball ball = cannon.shoot();
						allCannonballs.push_back(ball);
					};
						break;
					default:
						break;
					}
				}
				break;
			default:
				break;
			}
		}

		// add checks for landed cannonballs here,
		// also check for cannonballs hitting the target


		if ((allCannonballs.size() > 0) and (hitTarget(allCannonballs.back(),  target))) {
			gameOver = true;
		};

		for (int i = 0; i < allCannonballs.size(); i++) {
			if ((allCannonballs[i].hasLanded()) and not (gameOver)) {
				allCannonballs.erase(allCannonballs.begin()+i);
			};
		};
		

		// only update if game is not over
		if (!gameOver) {
			// update objects here

			target.update();
			cannon.update();
			for (int i = 0; i < allCannonballs.size(); i++) {
				allCannonballs[i].update();
			};
		}

		window.clear();
		// draw objects here

		target.draw(window);
		cannon.draw(window);
		for (int i = 0; i < allCannonballs.size(); i++) {
			allCannonballs[i].draw(window);
		};

		window.display();
	}
}

