from snake import Snake
from board import Board
from cell import Cell, Celltype

class Game():
    
    def __init__(self, board: Board, snake_body:Snake ):
        self._board = board
        self._game_over = False
        self._board.set_snake(snake_body)
        for cell in snake_body.get_snake():
            if not self.in_bounds(cell.get_row(), cell.get_col()) or cell.get_celltype() != Celltype.SNAKE:
                raise ValueError("Snake initial position is out of bounds or not free")
            self._board.get_board()[cell.get_row()][cell.get_col()] = cell
        self._snake = snake_body

    
    def get_board(self):
        return self._board

    
    def get_snake(self):
        return self._snake

    
    def is_game_over(self):
        return self._game_over

    def update(self, direction:str):
        if self._game_over:
            print("Game is over. Cannot update.")
            return
        delta = self.get_direction(direction)
        if not delta:
            print("Invalid direction. Use 'UP', 'DOWN', 'LEFT', or 'RIGHT'.")
            return
        head = self._snake.get_head()
        next_cell = self.get_next_cell(head, delta)
        if not next_cell:
            print("Next cell is out of bounds. Game over!")
            self._game_over = True
            return
        
        will_grow = next_cell.get_celltype() == Celltype.FOOD
        moved = self._snake.move(next_cell, will_grow)
        if not moved:
            print("Snake collided with itself. Game over!")
            self._game_over = True
            return
        elif will_grow:
            print("Snake ate food")
            self._board.generate_food()
        else:
            print("Snake moved into empty cell")
         
    def get_direction(self, direction:str):
        dirs = {
            "UP":    (-1, 0),
            "DOWN":  ( 1, 0),
            "LEFT":  ( 0,-1),
            "RIGHT": ( 0, 1),
        }
        return dirs.get(direction)
        
    def get_next_cell(self, curr_pos:Cell, direction:tuple):
        row, col = curr_pos.get_row(), curr_pos.get_col()
        next_row, next_col = row + direction[0], col + direction[1]
        
        if not self.in_bounds(next_row, next_col):
            return None
        
        return self._board.get_board()[next_row][next_col]

    def in_bounds(self, row:int, col:int):
        return 0 <= row < self._board._num_rows and 0 <= col < self._board._num_cols

if __name__ == "__main__":
    board = Board(5, 5)
    init_pos = Cell(2, 2, Celltype.SNAKE)
    snake = Snake(init_pos)
    game_instance = Game(board, snake)
    game_instance.get_board().generate_food()
    print(game_instance.get_board())
    
    while not game_instance.is_game_over():
        direction = input("Enter direction (UP, DOWN, LEFT, RIGHT): ").strip().upper()
        game_instance.update(direction)
        print(game_instance.get_board())
    