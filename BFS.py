from Board import Board
from SearchAlgo import SearchAlgo
from queue import PriorityQueue
import time
# open_list  is a Priority Queue

#same as dfs, except it sorts it's open list based on an heuristic
closed_list = {}
open_list = PriorityQueue()
goal_found_flag = False

class BFS(SearchAlgo):

  def __init__(self, board: Board, max_length: int, index: int):
    super().__init__(board, -1, index)
    self.max_length = max_length
    self.board.computeHeuristic(index)
    
  def search(self):
      global goal_found_flag
      global open_list
      global closed_list

      open_list.put(self.board)
      start_time = time.time()

      while not open_list.empty() and goal_found_flag is False:

          b = open_list.get()

          if b.puzzle_config in closed_list and closed_list[b.puzzle_config] < b.heuristic:
              continue
              # Now we need to check if it is an element that is already in closed list, if it is a lower heuristic that we found now then we replace it by lowest one.
          # Test
          print("\n")
          b.printBoard()
          print("\n")

          closed_list[b.puzzle_config] = b.heuristic
          #TODO: change this to display correct values (not 0 0 0 )
          self.search_file.write("0\t0\t0\t" + b.puzzle_config + "\n")

          if b.isGoal():
              print("Found it!\n") # Test
              print("--- %s seconds ---" % (time.time() - start_time))
              self.populate_solution_file(b)
              goal_found_flag = True

          elif b.depth < self.max_length:
              self.update_and_sort_open_list(b, open_list)

      if not goal_found_flag:
          self.solution_file.write("no solution")
          self.solution_file.close()

      goal_found_flag = False
      open_list = PriorityQueue()
      closed_list.clear()
      self.search_file.close()


  def update_and_sort_open_list(self, b:Board, open_list):
    for i in range(0, b.size * b.size):
        child_b = b.touch(i)
        child_b.computeHeuristic(i)
        open_list.put(child_b)
        
      # temp_arr = []
      # for i in range(0, b.size * b.size):
      #   child_b = b.touch(i)
      #   temp_arr.put((child_b.heuristic,child_b))
      #   # we dont wanna be sorting it au complet every single time tho
      # temp_arr.sort(reverse=True, key=lambda x: x.puzzle_config)
      # for i in temp_arr:
      #   open_list.put((i.heuristic, i))
