
# Hexagon Board Solver

This project implements a hexagonal board game where each hexagon can be connected to others, and pieces are placed according to specific rules. The solution is determined through backtracking, ensuring all constraints are satisfied.

---

## Features

1. **Hexagonal Board**:
   - Supports multiple hexagons with six possible connections each.
   - Enables dynamic connections between hexagons.

2. **Pieces with Constraints**:
   - Each piece has six values corresponding to its sides.
   - Placement is validated by matching the sides of adjacent pieces.

3. **Backtracking Solver**:
   - Uses recursion to solve the board by placing pieces satisfying all constraints.
   - Ensures all hexagons are filled with valid configurations.

4. **Visualization**:
   - Displays the solution with hexagon IDs and the pieces placed.

---

## Classes

### 1. `Hexagon`

Represents a single hexagon on the board.

#### Attributes:
- `id`: Unique identifier for the hexagon.
- `connections`: A list of six possible connections to other hexagons.
- `piece`: The piece currently placed on the hexagon.

#### Methods:
- `set_piece(piece)`: Assigns a piece to the hexagon.
- `remove_piece()`: Removes the piece from the hexagon.

---

### 2. `Board`

Manages the hexagonal board and handles the logic for solving.

#### Attributes:
- `hexagons`: List of all hexagons on the board.
- `OPPOSITE_SIDES`: Dictionary mapping sides to their opposite.

#### Methods:
- `add_hexagon(hexagon)`: Adds a hexagon to the board.
- `connect(hex1, side1, hex2)`: Connects two hexagons on specified sides.
- `solve(pieces)`: Solves the board using backtracking.
- `display_board_solution()`: Displays the solution.

---

### 3. `Piece`

Represents a piece with values for its six sides.

#### Attributes:
- `id`: Unique identifier for the piece.
- `values`: Dictionary with six keys (0 to 5) representing the sides and their values.

#### Methods:
- Validates the values to ensure they are in the allowed set.

---

## Installation

Ensure you have Python 3.7+ installed. No additional libraries are required.

---

## Usage

### Example
```python
# Create the board
board = Board()

# Add hexagons
hex1 = Hexagon(1)
hex2 = Hexagon(2)
hex3 = Hexagon(3)
board.add_hexagon(hex1)
board.add_hexagon(hex2)
board.add_hexagon(hex3)

# Connect hexagons
board.connect(hex1, 2, hex2)
board.connect(hex2, 3, hex3)

# Define pieces
pieces = [
    Piece(1, {0: "B3", 1: "B3", 2: "V2", 3: "V2", 4: "A3", 5: "A3"}),
    Piece(2, {0: "A1", 1: "A1", 2: "V2", 3: "V2", 4: "A3", 5: "A3"}),
    Piece(3, {0: "V2", 1: "V2", 2: "A3", 3: "A3", 4: "B3", 5: "B3"}),
]

# Solve the board
if board.solve(pieces):
    board.display_board_solution()
else:
    print("No solution found.")
```

---

## Contribution

Feel free to fork and enhance this project. Suggestions and bug fixes are welcome!

---

## License

This project is licensed under the MIT License.
