from Board import Board
from pathlib import Path
from abc import ABC, abstractmethod

class SearchAlgo(ABC):
    def __init__(self, board: Board, max_depth: int, index: int):
        self.board = board
        self.max_depth = max_depth
        # see the convo

        ## File creation
        Path("Outputs").mkdir(parents=True, exist_ok=True)

        algo_name = type(self).__name__.lower()

        # Search file
        file_name_dfs_search = "Outputs/" + str(index) + "_" + algo_name + "_search.txt"
        self.search_file = open(file_name_dfs_search, "w+")

        # Solution file
        file_name_dfs_solution = "Outputs/" + str(index) + "_" + algo_name + "_solution.txt"
        self.solution_file = open(file_name_dfs_solution, "w+")

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

    @abstractmethod
    def search(self):
        pass

    @abstractmethod
    def update_and_sort_open_list(self, b:Board, open_list):
        pass

    def getSearchOutput(self, g, h, board):
        return "{}\t{}\t{}\t{}\n".format(int(g+h), g, h, board)
