#include "Minesweeper.h"
#include "utilities.h"

Minesweeper::Minesweeper(int width, int height, int mines) {
	// Declare the grid (by default closed and no mines)
	columns = width;
	rows = height;
	bombs = mines;
	grid = new Tile*[rows];
	for (int i = 0; i < rows; i++) {
		grid[i] = new Tile[columns];
	};
	// Randomly place mines
	int remainingMines = mines;
	int rowPlace;
	int colPlace;
	while (remainingMines > 0) {
		rowPlace = randomWithLimits(0, rows - 1);
		colPlace = randomWithLimits(0, columns - 1);
		if (not grid[rowPlace][colPlace].mine) {
			grid[rowPlace][colPlace].mine = true;
			remainingMines -= 1;
		};
	};
}

Minesweeper::~Minesweeper() {
	for (int i = 0; i < rows; i++) {
		delete[] grid[i];
	};
	delete[] grid;
	grid = nullptr;
}

bool Minesweeper::isGameOver() const {
	for (int i = 0; i < columns; i++) {
		for (int j = 0; j < rows; j++) {
			if (grid[i][j].mine and grid[i][j].open) {
				return true;
			};
		};
	};
	return false;
}

bool Minesweeper::isTileOpen(int row, int col) const {
	return grid[row][col].open;
}

bool Minesweeper::isTileMine(int row, int col) const {
	return grid[row][col].mine;
}

// Added
bool Minesweeper::isTileFlagged(int row, int col) const {
	return grid[row][col].flagged;
}

void Minesweeper::openTile(int row, int col) {
	if ((not grid[row][col].open) and (not grid[row][col].flagged)) {
		grid[row][col].open = true;
		if ((not grid[row][col].mine) and (numAdjacentMines(row, col) == 0)) {
			for (int i = row - 1; i <= row + 1; i++) {
				for (int j = col - 1; j <= col + 1; j++) {
					if (not ((i < 0) or (i >= rows) or (j < 0) or (j >= columns))) {
						openTile(i, j);
					}
				}
			}
		}
	}
}

int Minesweeper::numAdjacentMines(int row, int col) const {
	int counter = 0;
	for (int i = row - 1; i <= row + 1; i++) {
		for (int j = col - 1; j <= col + 1; j++) {
			if (not ((i < 0) or (i >= rows) or (j < 0) or (j >= columns))) {
				if (isTileMine(i, j)) {
					counter += 1;
				}
			}
		}
	}
	return counter;
}

// Extra funcitons
int Minesweeper::numTilesRemaining() const {
	int counter = 0;
	for (int i = 0; i < columns; i++) {
		for (int j = 0; j < rows; j++) {
			if (not grid[i][j].open) {
				counter += 1;
			}
		}
	}
	return counter;
}
int Minesweeper::getBombs() const {
	return bombs;
}
void Minesweeper::flagTile(int row, int col) {
	grid[row][col].flagged = !grid[row][col].flagged;
}