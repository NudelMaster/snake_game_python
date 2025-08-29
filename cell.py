from enum import Enum, auto

class Celltype(Enum):
    EMPTY = auto()
    SNAKE = auto()
    FOOD = auto()


class Cell():

    def __init__(self, row:int, col:int, celltype:Celltype):
        self._row = row
        self._col = col
        self._celltype = celltype

    
    def get_row(self):
        return self._row
   
    def get_col(self):
        return self._col
    
    def get_celltype(self):
        return self._celltype
    
    def set_celltype(self, celltype:Celltype):
        self._celltype = celltype
    
    


    


    


