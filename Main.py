from Board import Board
from DFS import DFS
from BFS import BFS

def main():
    for line_number, element in enumerate(get_input("input.txt")):
        print(element)

        # Create root node
        board = Board(int(element[0]), element[3], None, 0,  1)
        max_depth = int(element[1])
        max_length = int(element[2])

        # DFS
        dfs = DFS(board, max_depth, line_number)
        dfs.search()

        #BFS
        bfs = BFS(board, max_length, line_number)
        bfs.search()

def get_input(input_file):
    input_list = []
    with open(input_file) as file:
        for line in file:
            puzzle_config = line.split()
            if len(puzzle_config) != 4:
                raise Exception("Incorrect input format. Verify file: " + input_file)
            input_list.append(line.split())
    return input_list


main()