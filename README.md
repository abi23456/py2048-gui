# 2048 Game GUI Implementation

## Overview
This project is a graphical user interface (GUI) implementation of the popular game 2048. The objective of the game is to combine tiles with the same number to reach the tile with the value of 2048. The game features a 4x4 board and allows players to slide tiles in four directions: up, down, left, and right.

## Features
- **Board Initialization**: The game starts with a 4x4 board and two random tiles with values of 2 or 4.
- **Game Mechanics**: Players can move tiles, merge them, and a new tile appears after each move.
- **Scoring System**: The score is tracked based on merged tiles.
- **Game End Conditions**: The game ends when the player reaches 2048 or when no more moves are possible.
- **Restart Option**: Players can restart the game from the GUI.

## Installation
1. Clone the repository:
   ```
   git clone https://github.com/yourusername/py2048-gui.git
   ```
2. Navigate to the project directory:
   ```
   cd py2048-gui
   ```
3. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

## Running the Game
To start the game, run the following command:
```
python src/main.py
```

## Gameplay Instructions
- Use the arrow keys or GUI buttons to slide the tiles.
- Combine tiles with the same number to increase your score.
- Aim to reach the 2048 tile to win the game.

## Implementation Details
- The project is structured into several modules, each handling different aspects of the game:
  - `main.py`: Entry point for the application.
  - `game.py`: Contains the main game logic.
  - `board.py`: Manages the game board.
  - `moves.py`: Handles tile movements.
  - `score.py`: Manages the scoring system.
  - `state.py`: Handles game state management.
  - `utils.py`: Contains utility functions.
  - `gui/`: Contains all GUI-related files.

## Contribution
Feel free to contribute to the project by submitting issues or pull requests.

## License
This project is licensed under the MIT License. See the LICENSE file for more details.