from Board import Board;

closedList = set()
goal_found_flag = False

# This method takes a file name as input and returns a list with the puzzle configurations
def get_input(inputFile):
    input_list = []
    with open(inputFile) as file:
        for line in file:
            puzzle_config = line.split()
            if len(puzzle_config) != 4:
                raise Exception("Incorrect input format. Verify file: " + inputFile)
            input_list.append(line.split())
    print(input_list)
    return input_list

def dfs_max_depth(board: Board, curr_depth: int, max_depth: int):
    global goal_found_flag
    open_list = []

    if should_stop_looking(curr_depth, max_depth, board):
        return

    print("\n")
    board.printBoard()
    print("\n")

    closedList.add(board)

    if board.isGoal():
        print("Found it!\n")
        goal_found_flag = True
    else:
        for i in range(0, board.size*board.size):
            open_list.append(board.touch(i))
        open_list.sort(key=lambda x: x.puzzle_config)
        for board in open_list:
            dfs_max_depth(board, curr_depth + 1, max_depth)

def should_stop_looking(curr_depth: int, max_depth : int, board: Board):
    return goal_found_flag or curr_depth >= max_depth or closedList.__contains__(board)
# test code to verify working code
def test():
    global goal_found_flag
    print("Test the getInput() method")
    print("===========================")
    for element in get_input("input.txt"):
        print(element)
        # Create root node
        board = Board(int(element[0]), element[3], None, 0)
        board.printBoard()
        max_depth = int(element[1])
        dfs_max_depth(board, 1, max_depth)
        goal_found_flag = False

test()
