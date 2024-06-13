# Island Perimeter

This project contains a function to calculate the perimeter of an island in a grid.

## Function

- `island_perimeter(grid)`: Calculates the perimeter of the island described in the grid.

## Grid Description

- `0` represents water.
- `1` represents land.
- Each cell is a square with side length 1.
- Cells are connected horizontally/vertically (not diagonally).
- The grid is rectangular with width and height not exceeding 100.
- The grid is completely surrounded by water.
- There is only one island (or nothing).
- The island doesn't have lakes (water inside that isn't connected to the water surrounding the island).

## Example

```python
grid = [
    [0, 0, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, 0],
    [0, 1, 1, 1, 0, 0],
    [0, 0, 0, 0, 0, 0]
]
print(island_perimeter(grid))  # Output: 12
