from cell import Cell, Celltype
from collections import deque

class Snake():

    def __init__(self, init_pos:Cell):
        self.body = deque([init_pos])
        init_pos.set_celltype(Celltype.SNAKE)
        self.body_parts = {init_pos} # for O(1) lookups
        print(f"Initialized snake at ({init_pos.get_row()}, {init_pos.get_col()})")

        
    def get_head(self):
        return self.body[0]
    def move(self, next_cell:Cell, grow:bool):
        print(f"Moving snake to {next_cell.get_row()}, {next_cell.get_col()}")

        moving_into_tail_exception = (not grow) and (next_cell == self.body[-1])
        if self.check_collision(next_cell) and not moving_into_tail_exception:
            return False
        
        
        if not grow:
            tail = self.body.pop()
            tail.set_celltype(Celltype.EMPTY)
            self.body_parts.remove(tail)
        
        
        head = next_cell
        head.set_celltype(Celltype.SNAKE)
        self.body.appendleft(head)
        self.body_parts.add(head)
        return True
    def check_collision(self, next_cell:Cell):
        if next_cell in self.body_parts:
            return True
        return False
    
    def get_snake(self):
        return self.body
    
    def set_snake(self, body:deque):
        self.body = body
        self.body_parts = set(body)

    
        
        



        
        