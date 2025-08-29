from cell import Cell, Celltype
from snake import Snake
import random
class Board():
    def __init__(self, num_rows:int, num_cols:int):
        self._num_rows = num_rows
        self._num_cols = num_cols
        self._board = [[Cell(row, col, Celltype.EMPTY) for col in range(num_cols)] for row in range(num_rows)]
    
    def get_board(self):
        return self._board

    def set_board(self, board):
        self._board = board
    def set_snake(self, snake: Snake):
        self._snake = snake
    def generate_food(self):
        print("Generating food")
        row = col = 0
        while True:
            row = random.randint(0, self._num_rows - 1)
            col = random.randint(0, self._num_cols - 1)
            if self._board[row][col].get_celltype() == Celltype.EMPTY:
                self._board[row][col].set_celltype(Celltype.FOOD)
                break
        print(f"Food generated at ({row}, {col})")
    
    def __repr__(self):
        board_str = ""
        for row in self._board:
            for cell in row:
                if cell.get_celltype() == Celltype.EMPTY:
                    board_str += ". "
                elif cell.get_celltype() == Celltype.SNAKE:
                    if cell == self._snake.get_head():
                        board_str += "H "
                    else:
                        board_str += "S "
                elif cell.get_celltype() == Celltype.FOOD:
                    board_str += "F "
            board_str += "\n"
        return board_str