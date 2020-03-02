from Board import Board
from BFS import BFS 
import time
from queue import PriorityQueue

closed_list = {}
open_list = PriorityQueue()
goal_found_flag = False

class ASTAR(BFS):
    def search(self):
      global goal_found_flag
      global open_list
      global closed_list

      open_list.put(self.board)
      start_time = time.time()

      while not open_list.empty() and goal_found_flag is False:

          b = open_list.get()

          if b.puzzle_config in closed_list and closed_list[b.puzzle_config] <= b.depth:
            continue

          # Test
          print("\n")
          b.printBoard()
          print("\n")

          closed_list[b.puzzle_config] = b.depth

          self.search_file.write(self.getSearchOutput(b.depth, b.heuristic, b))

          if b.isGoal():
              print("Found it!\n") # Test
              print("--- %s seconds ---" % (time.time() - start_time))
              self.populate_solution_file(b)
              goal_found_flag = True

          elif closed_list.__len__() < self.max_length:
              self.update_and_sort_open_list(b, open_list)

      if not goal_found_flag:
          self.solution_file.write("no solution")
          self.solution_file.close()

      goal_found_flag = False
      open_list = PriorityQueue()
      closed_list.clear()
      self.search_file.close()

    def __init__(self, board: Board, max_length: int, index: int):
        super().__init__(board, -1, index)
        self.max_length = max_length
        self.board.computeF()

    def update_and_sort_open_list(self, b: Board, open_list):
        for i in range(0, b.size * b.size):
            child_b = b.touch(i)
            child_b.computeF()
            open_list.put(child_b)