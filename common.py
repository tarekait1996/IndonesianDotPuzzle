from Board import Board;

closedList = set()  ## hashSet
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
    global closedList
    open_list.append(board)

    while len(open_list) != 0 and goal_found_flag is False:

        b = open_list.pop()

        print("\n")
        b.printBoard()
        print("\n")

        if closedList.__contains__(b.puzzle_config):
            continue

        closedList.add(b.puzzle_config)

        if b.isGoal():
            print("Found it!\n")
            goal_found_flag = True

        elif b.depth < max_depth:
            temp_arr = []
            for i in range(0, b.size * b.size):
                c_board = board.touch(i)
                c_board.depth = c_board.depth+1
                temp_arr.append(c_board)
            temp_arr.sort(reverse=True, key=lambda x: x.puzzle_config)
            open_list.extend(temp_arr)


# test code to verify working code
def test():
    global goal_found_flag
    print("Test the getInput() method")
    print("===========================")
    for element in get_input("input.txt"):
        print(element)
        # Create root node
        board = Board(int(element[0]), element[3], None)

        max_depth = int(element[1])
        dfs_max_depth(board, max_depth)
        goal_found_flag = False


test()
