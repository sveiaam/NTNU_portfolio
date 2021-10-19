#pragma once


struct Tile {
	bool open = false;
	bool mine = false;
	bool flagged = false;
};


class Minesweeper {
private:
	Tile **grid;
	int rows;
	int columns;
	int bombs;

public:
	Minesweeper(int width, int height, int mines);
	~Minesweeper();

	bool isGameOver() const;

	bool isTileOpen(int row, int col) const;
	bool isTileMine(int row, int col) const;

	void openTile(int row, int col);

	int numAdjacentMines(int row, int col) const;

	// Vi slår av autogenerert kopikonstruktør og tilordningsoperator for å unngå feil
	Minesweeper(const Minesweeper &) = delete;
	Minesweeper &operator=(const Minesweeper &) = delete;

	// Extra functions
	int numTilesRemaining() const;
	int getBombs() const;
	void flagTile(int row, int col);
	bool isTileFlagged(int row, int col) const;
};
