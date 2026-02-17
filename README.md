# Knight's Move Game ♞

A simple Python implementation of a chess knight's movement visualization and validation. The project includes an interactive game where users can move a knight on an 8x8 chessboard and a unit test suite to verify the knight's movement logic.

## Project Structure 📁

- `knight_game.py` - Main game file with interactive knight movement
- `test knight game.py` - Unit tests for the knight's movement validation
- `README.md` - Project documentation

## Features ✨

### Interactive Game (`knight_game.py`)
- Visual 8x8 chessboard display
- Shows current knight position (K) and valid moves (*)
- Validates user input against chess knight movement rules
- Interactive gameplay with position input

### Test Suite (`test knight game.py`)
- Verifies knight movement from various board positions:
  - Center position (4,4) - 8 possible moves
  - Corner position (0,0) - 2 possible moves  
  - Edge position (0,1) - 3 possible moves
- Uses Python's `unittest` framework

## How to Play 🎮

1. Run the game:
```bash
python knight_game.py