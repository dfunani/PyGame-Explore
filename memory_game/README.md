# PyMemory: A Fun Memory Game in Python

**PyMemory** is a beginner-friendly Python game that challenges your memory and reflexes. Your goal is to find matching pairs of shapes hidden on a board by flipping them over. Uncover all the pairs before time runs out to win!

This README provides an overview of the project's structure and functionality for those new to Python development.

## Installation

There are no external dependencies to install. However, you'll need Python 3.x installed on your system.

## Getting Started

1. Clone this repository:

```Bash
git clone https://github.com/dfunani/pymemory.git
```

2. Navigate to the project directory:

```Bash
cd pymemory
```

3. Run the game:

```Bash
python -m pip install -r requirements.txt
python app.py
```

## How to Play

The game window will display a grid of squares hiding different shapes (emojis in this version). Click a square to reveal its shape. Try to remember the location of matching shapes. Click on another square to try and find its pair. If the shapes match, they'll remain revealed. If not, they'll both be hidden again.

Keep flipping squares and matching pairs until all shapes are revealed. You'll have a limited amount of time to complete the challenge. The game will display a message indicating whether you won or lost.

## Project Structure

This project is organized into several Python files:

- [_app.py_](./app.py): The main entry point for the game. It initializes the player, board, and game manager, and starts the game loop.
- [_models/colors.py_](./models/colors.py): Defines an enumeration class Colors to represent the different colors used in the game.
- [_models/exceptions.py_](./models/exceptions.py): Defines custom exceptions (ShapeGeneratorError and GameManagerError) used in the game.
- [_models/players.py_](./models/players.py): Defines a class PlayerManager to handle player interactions like mouse clicks.
- [_models/shapes.py_](./models/shapes.py): Defines an enumeration class Shapes containing all the different emojis used as shapes in the game.
- [_managers/board.py_](./managers/board.py): Defines a class BoardManager to manage the game board, including generating the board layout and handling board interactions (like checking for box collisions).
- [_managers/game.py_](./managers/game.py): Defines a class GameManager to manage the overall game flow, including setting up the game window, handling player input, and displaying the result (win/lose).
- [_managers/player.py_](./managers/player.py): Contains the PlayerManager class definition as described above.

## Additional Notes

This is a basic implementation of the memory game. You can extend it further by:

1. Implementing different difficulty levels with more shapes or a larger board.
2. Adding sound effects and background music.
3. Introducing different game modes with variations in gameplay.

Feel free to explore the code and experiment with modifications!
