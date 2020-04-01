from contextlib import contextmanager
from time import time, sleep
from sudoku_solver import solve
import os

@contextmanager
def timer():
    start_time = time()
    yield
    total_time = time() - start_time
    print(f'Elapsed time: {total_time:.8f}s')

def batch_solve(puzzles):
    return [solve(puzzle) for puzzle in puzzles]

sudoku_puzzles_file = os.path.join('puzzles', 'sudoku-topn234.txt')
with open(sudoku_puzzles_file) as file:
    puzzles = [line.strip() for line in file]

with timer():
    batch_solve(puzzles)
