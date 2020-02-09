from Board import Board;

closed_list = []  ## i need something ordered
open_list = []  ## Stack
goal_found_flag = False

# This method takes a file name as input and returns a list with the puzzle configurations
def get_input(input_file):
    input_list = []
    with open(input_file) as file:
        for line in file:
            puzzle_config = line.split()
            if len(puzzle_config) != 4:
                raise Exception("Incorrect input format. Verify file: " + input_file)
            input_list.append(line.split())
    return input_list


def dfs_max_depth(board: Board, max_depth: int):
    global goal_found_flag
    global open_list
    global closed_list

    open_list.append(board)

    while len(open_list) != 0 and goal_found_flag is False:

        b = open_list.pop()

        if closed_list.count(b.puzzle_config) != 0:
            continue
        print("\n")
        b.printBoard()
        print("\n")
        closed_list.append(b.puzzle_config)

        if b.isGoal():
            print("Found it!\n")
            goal_found_flag = True

        elif b.depth < max_depth:
            temp_arr = []
            for i in range(0, b.size * b.size):
                temp_arr.append(b.touch(i))
            temp_arr.sort(reverse=True, key=lambda x: x.puzzle_config)
            open_list.extend(temp_arr)

def should_stop_looking(curr_depth: int, max_depth : int, board: Board):
    return goal_found_flag or curr_depth >= max_depth or closed_list.count(board) != 0


def test_dfs():
    global goal_found_flag
    line_number = 0 #TODO: check if there is a way of knowing the index without a counter
    
    for element in get_input("input.txt"):
        print(element)

        # Files creation
        # file_name_dfs_solution = "Outputs/" + str(line_number) + "_dfs_solution.txt"
        # file_dfs_solution = open(file_name_dfs_solution, "w+")

        file_name_dfs_search = "Outputs/" + str(line_number) + "_dfs_search.txt"
        file_dfs_search = open(file_name_dfs_search, "w+")

        # Create root node
        board = Board(int(element[0]), element[3], None, 0,  1)
        max_depth = int(element[1])

        # DFS
        dfs_max_depth(board, max_depth)
        for element in closed_list:
          file_dfs_search.write(str(element.touch_idx) + " " + str(element.puzzle_config) + "\n")

        line_number = line_number + 1
        goal_found_flag = False
        open_list.clear()
        closed_list.clear()


test_dfs()