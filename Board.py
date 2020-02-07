# Board represents the nodes in our tree
class Board:
    # precondition: size should be limited to maxium 26 (A-Z)
    def __init__(self, size, puzzle_config, parent, touch_idx):
        self.size = size
        self.puzzle_config = puzzle_config
        self.parent = parent
        self.touch_idx = touch_idx

    def getPosition(self, index):
        # According to the this (http://www.asciitable.com/), A-Z have codes between 65 and 90
        # Mapping: row 1 -> A(65), row 2 -> B(66), etc...
        row = (index // self.size) + 1
        column = (index % self.size) + 1
        row_letter = chr(row + 64)
        return row_letter + str(column)

    def touch(self, index):
        new_config = self.switchTokenAt(index, self.puzzle_config)
        new_config = self.switchTokenAt(self.getTop(index), new_config)
        new_config = self.switchTokenAt(self.getRight(index), new_config)
        new_config = self.switchTokenAt(self.getBottom(index), new_config)
        new_config = self.switchTokenAt(self.getLeft(index), new_config)
        return Board(self.size, new_config, self, index)

    def switchTokenAt(self, index, board):
        if index == -1:
            return board
        else:
            resulting_board = board[:index] + str(1-int(board[index])) + board[index + 1:]
            return resulting_board

    def getTop(self, index):
        if index - self.size < 0:
            return -1
        else:
            return index - self.size

    def getRight(self, index):
        if (index + 1) % (self.size) == 0:
            return -1
        else:
            return index + 1

    def getBottom(self, index):
        if (index + self.size) > (self.size * self.size - 1):
            return -1
        else:
            return index + self.size

    def getLeft(self, index):
        if index % self.size == 0:
            return -1
        else:
            return index - 1

    def isRoot(self):
        return self.parent is None

    def isGoal(self):
        return self.puzzle_config.count('0') == self.size * self.size

    def printBoard(self):
        j = 0
        res = "\n"
        for i in list(self.puzzle_config):
            res += i + " "
            if (j + 1) % self.size == 0:
                res += "\n"
            j += 1
        print(res)

    def toString(self):
        return self.getPosition(self.touch_idx) + "\t" + self.puzzle_config
