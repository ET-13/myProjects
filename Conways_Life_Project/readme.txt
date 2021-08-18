The "Game of Life" was created by a British mathematician in 1970, named John Horton Conway.
It is meant to represent the creation, destruction and development of life in the form of cells.

Every cell interacts with neighbors, cells which are horizontally, verically or diagonally adjacent to each other.
Each cell has two possible states, alive or dead (populated or unpopulated)

The rules are as follows:

1) Any live cell with fewer than two live neighbors will die "underpopulation"
2) Any live cell with two or three live neighbors lives on to the next generation.
3) Any live cell with more than (over) three live neighbors will die "overpopulation"
4) Any dead cell with exactly three neighbors, will become a live cell "reproduction"

This program seeks to recreate Conway's game of life. It has been done before and this is my own attempt.

For this we need a space (grid) we can populate with elements
The above rules to change the state of this element in our simulation
A way to view the simulation or record the progression of the cells

It seems like given our starting parameters, the simulation eventually reaches a still-life, no matter the size of the grid or any other changing value other than the starting parameters

I think there may be an issue with cell generation though, I'll fix it later. This is a WIP for now.
