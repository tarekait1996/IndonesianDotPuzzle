from Board import Board
from pathlib import Path

closed_list = set()
open_list = []
goal_found_flag = False


class DFS:
    def __init__(self, board: Board, max_depth: int, index: int):
        self.board = board
        self.max_depth = max_depth

        ## File creation
        Path("Outputs").mkdir(parents=True, exist_ok=True)

        # Search file
        file_name_dfs_search = "Outputs/" + str(index) + "_dfs_search.txt"
        self.search_file = open(file_name_dfs_search, "w+")

        # Solution file
        file_name_dfs_solution = "Outputs/" + str(index) + "_dfs_solution.txt"
        self.solution_file = open(file_name_dfs_solution, "w+")

    def search(self):
        global goal_found_flag
        global open_list
        global closed_list

        open_list.append(self.board)

        while len(open_list) != 0 and goal_found_flag is False:

            b = open_list.pop()

            if closed_list.__contains__(b.puzzle_config):
                continue

            # Test
            print("\n")
            b.printBoard()
            print("\n")

            closed_list.add(b.puzzle_config)
            self.search_file.write("0\t0\t0\t" + b.puzzle_config + "\n")

            if b.isGoal():
                print("Found it!\n") # Test
                self.populate_solution_file(b)
                goal_found_flag = True

            elif b.depth < self.max_depth:
                temp_arr = []
                for i in range(0, b.size * b.size):
                    temp_arr.append(b.touch(i))
                temp_arr.sort(reverse=True, key=lambda x: x.puzzle_config)
                open_list.extend(temp_arr)

        if not goal_found_flag:
            self.solution_file.write("no solution")
            self.solution_file.close()

        goal_found_flag = False
        open_list.clear()
        closed_list.clear()
        self.search_file.close()

    def populate_solution_file(self, board: Board):
        solution_list = []
        key_value_pair = {board.getPosition(board.touch_idx): board.puzzle_config}
        solution_list.append(key_value_pair)

        while not board.isRoot():
            board = board.parent
            key_value_pair = {board.getPosition(board.touch_idx): board.puzzle_config}
            solution_list.append(key_value_pair)

        solution_list.reverse()

        first_flag = True
        for pair in solution_list:
            position = list(pair.keys())[0]
            config = list(pair.values())[0]

            if first_flag:
                self.solution_file.write("0 " + config + "\n")
                first_flag = False
            else:
                self.solution_file.write(str(position) + " " + config + "\n")

        self.solution_file.close()