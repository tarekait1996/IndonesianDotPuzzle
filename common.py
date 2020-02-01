from Board import Board;

# This method takes a file name as input and returns a list with the puzzle configurations
MAX_DEPTH = 0


def get_input(inputFile):
    inputList = []
    with open(inputFile) as file:
        for line in file:
            puzzle_config = line.split()
            if len(puzzle_config) != 4:
                raise Exception("Incorrect input format. Verify file: " + inputFile)
            inputList.append(line.split())
    return inputList


def dfs_max_depth(board: Board, curr_depth: int):
    if curr_depth > MAX_DEPTH:
        return
    if board.isGoal():
        foundIt()
    for i in range(0, board.size + 1):
        dfs_max_depth(board.touch(i), curr_depth + 1)


# just for now
def foundIt():
    return


# test code to verify working code
def test():
    print("Test the getInput() method")
    print("===========================")
    for element in get_input("input.txt"):
        print(element)
        # Create root node
        board = Board(int(element[0]), element[3], None)

        MAX_DEPTH = element[1]
        print("Alphanumeric positon at index 3 [testing method getPostion()]: " + board.getPosition(3))
        print("\n[testing printBoard()]\nOriginal Config:")
        board.printBoard()
        print("Is this the root? " + str(board.isRoot()))
        print("Is this the goal? " + str(board.isGoal()))

        print("\n---Touch index 6!---")
        print("\n[testing touch()]\nResulting Config:")
        child = board.touch(6)
        child.printBoard()
        print("Is this the root? " + str(child.isRoot()))
        print("Is this the goal? " + str(child.isGoal()))
        print("===========================")

    print("===========================")
    print("[Testing method isGoal()]")
    goal = Board(3, '000000000', None)
    goal.printBoard();
    print("Is this the goal? " + str(goal.isGoal()))


test();
