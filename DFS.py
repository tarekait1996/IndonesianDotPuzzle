from Board import Board
from pathlib import Path
from SearchAlgo import SearchAlgo

closed_list = {}
open_list = []
goal_found_flag = False

class DFS(SearchAlgo):
    def search(self):
        global goal_found_flag
        global open_list
        global closed_list

        open_list.append(self.board)

        while len(open_list) != 0 and goal_found_flag is False:

            b = open_list.pop()

            if b.puzzle_config in closed_list and closed_list[b.puzzle_config] < b.depth:
                continue

            # Test
            print("\n")
            b.printBoard()
            print("\n")

            closed_list[b.puzzle_config] = b.depth
            self.search_file.write("0\t0\t0\t" + b.puzzle_config + "\n")

            if b.isGoal():
                print("Found it!\n") # Test
                self.populate_solution_file(b)
                goal_found_flag = True

            elif b.depth < self.max_depth:
                print("this should be printed")
                self.update_and_sort_open_list(b, open_list)

        if not goal_found_flag:
            self.solution_file.write("no solution")
            self.solution_file.close()

        goal_found_flag = False
        open_list.clear()
        closed_list.clear()
        self.search_file.close()


    def update_and_sort_open_list(self, b:Board, open_list):
        temp_arr = []
        for i in range(0, b.size * b.size):
            temp_arr.append(b.touch(i))
        temp_arr.sort(reverse=True, key=lambda x: x.puzzle_config)
        open_list.extend(temp_arr)
