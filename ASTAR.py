from Board import Board
from BFS import BFS
# same as bfs, except it will calculate f(n) = g(n) + h(n)
class ASTAR(BFS):
    def __init__(self, board: Board, max_length: int, index: int):
        super().__init__(board, -1, index)
        self.max_length = max_length
        self.board.computeF()

    def update_and_sort_open_list(self, b: Board, open_list):
        for i in range(0, b.size * b.size):
            child_b = b.touch(i)
            child_b.computeF()
            open_list.put(child_b)