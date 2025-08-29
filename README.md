# Python Snake Game

A simple terminal-based Snake game implementation in Python using object-oriented programming principles.

## Game Description

This is a classic Snake game where the player controls a snake that moves around the board. The snake can eat food (F) to grow longer and must avoid colliding with walls or itself.

### Game Elements
- `H`: Snake head
- `S`: Snake body
- `F`: Food
- `.`: Empty cell

## Game Rules

1. The snake continuously moves in the direction specified by the player
2. Use UP, DOWN, LEFT, RIGHT commands to control the snake's direction
3. Eating food (F) makes the snake grow longer
4. Game ends if the snake:
   - Hits the board boundaries
   - Collides with itself

## Project Structure

- `game.py`: Main game logic and control flow
- `board.py`: Board representation and food generation
- `snake.py`: Snake movement and collision detection
- `cell.py`: Cell types and properties

## How to Play

1. Run the game:
```bash
python game.py
```

2. Enter directions using:
   - UP
   - DOWN
   - LEFT
   - RIGHT

3. Try to eat as much food as possible without colliding!

## Game Components

### Board Class
- Manages the game board
- Generates food at random empty positions
- Displays current game state

### Snake Class
- Handles snake movement
- Manages snake growth
- Detects collisions

### Cell Class
- Represents board positions
- Has three states: EMPTY, SNAKE, FOOD

### Game Class
- Controls game flow
- Processes user input
- Updates game state

## Example Game Board
```
. . . . . 
. H S . . 
. . F . . 
. . . . . 
. . . . . 
```

## Requirements
- Python 3.x
- No external dependencies required
