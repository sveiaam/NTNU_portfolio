#include "utilities.h"
#include <cstdlib>
#include <ctime>

//5a
int randomWithLimits(int minLim, int maxLim) {
	int diff = maxLim - minLim;
	int num = std::rand() % (diff+1) + minLim;
	return num;
}