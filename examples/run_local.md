# Instructions for Running the 2048 Game Locally

This document provides step-by-step instructions for running the 2048 game locally on your machine.

## Prerequisites

Before running the game, ensure you have the following installed:

- Python 3.6 or higher
- pip (Python package installer)

## Installation Steps

1. **Clone the Repository**

   Open your terminal and clone the repository using the following command:

   ```
   git clone https://github.com/yourusername/py2048-gui.git
   ```

   Replace `yourusername` with your GitHub username.

2. **Navigate to the Project Directory**

   Change into the project directory:

   ```
   cd py2048-gui
   ```

3. **Install Dependencies**

   Install the required packages using pip:

   ```
   pip install -r requirements.txt
   ```

4. **Run the Game**

   To start the game, execute the following command:

   ```
   python src/main.py
   ```

   This will launch the GUI for the 2048 game.

## Gameplay Instructions

- Use the arrow keys on your keyboard to slide the tiles in the desired direction (up, down, left, right).
- Tiles with the same number will merge into one when they collide.
- The goal is to reach the tile with the value of 2048.
- A new tile (2 or 4) will appear after each move.
- The game ends when there are no more valid moves available or when you reach 2048.

## Troubleshooting

- If you encounter any issues, ensure that all dependencies are installed correctly.
- Check the terminal for any error messages that may indicate what went wrong.

Enjoy playing 2048!