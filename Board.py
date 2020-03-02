class Board:
    # precondition: size should be limited to maxium 26 (A-Z)
    def __init__(self, size, puzzle_config, parent, touch_idx, depth):
        self.size = size
        self.depth = depth
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
        return Board(self.size, new_config, self, index, self.depth +1)

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

    def computeHeuristic(self):
      self.heuristic = self.computeCost_H()

    def computeF(self):
      self.heuristic = self.computeCost_H() + self.depth

    def computeCost_H(self):
        return self.computeCost_H3()

    # Different heuristics that can be used to calculate cost
    def computeCost_H1(self):
        return self.puzzle_config.count('1')

    def computeCost_H2(self):
      sum = 0
      index = self.touch_idx

      left = self.getLeft(index)
      right = self.getRight(index)
      top = self.getTop(index)
      bottom = self.getBottom(index)
  
      sum += (int(self.puzzle_config[index]))
  
      if(left > 0):
          sum += int(self.puzzle_config[left])
      if (right > 0):
          sum += int(self.puzzle_config[right])
      if (top > 0):
          sum += int(self.puzzle_config[top])
      if (bottom > 0):
          sum += int(self.puzzle_config[bottom])
      return sum

    def computeCost_H3(self):
        return 2*(self.getNumberOfOnes() + self.getNumberOfClusters())/5

    def computeCost_H4(self):
        return (self.getNumberOfOnes() + self.getNumberOfClusters())/6

    def getNumberOfOnes(self):
        return self.puzzle_config.count('1')

    def getNumberOfClusters(self):
        number = 0
        copy_config = self.puzzle_config[:]
        for i in range(0, self.size * self.size):
            if copy_config[i] == '1':
                copy_config = self.numOfClustersHelper(i, copy_config)
                number += 1
        return number

    def numOfClustersHelper(self, index, copy_config):
        left = self.getLeft(index)
        right = self.getRight(index)
        top = self.getTop(index)
        bottom = self.getBottom(index)

        copy_config = copy_config[:index] + '0' + copy_config[index + 1:]

        if left > 0 and copy_config[left] == '1':
            copy_config = self.numOfClustersHelper(left, copy_config)
        if right > 0 and copy_config[right] == '1':
            copy_config = self.numOfClustersHelper(right, copy_config)
        if top > 0 and copy_config[top] == '1':
            copy_config = self.numOfClustersHelper(top, copy_config)
        if bottom > 0 and copy_config[bottom] == '1':
            copy_config = self.numOfClustersHelper(bottom, copy_config)
        return copy_config

    def printBoard(self):
        j = 0
        res = "\n"
        for i in list(self.puzzle_config):
            res += i + " "
            if (j + 1) % self.size == 0:
                res += "\n"
            j += 1
        print(res)

    # Comparators (PQ uses these comparators to sort)
    def __eq__(self, other):
        return self.heuristic == other.heuristic and self.puzzle_config == other.puzzle_config

    def __ne__(self, other):
        return self.heuristic != other.heuristic

    def __lt__(self, other):
        return self.heuristic < other.heuristic or (self.heuristic == other.heuristic and self.puzzle_config < other.puzzle_config)

    def __le__(self, other):
        return self.heuristic < other.heuristic or (self.heuristic == other.heuristic and self.puzzle_config <= other.puzzle_config)

    def __gt__(self, other):
        return self.heuristic > other.heuristic or (self.heuristic == other.heuristic and self.puzzle_config > other.puzzle_config)

    def __ge__(self, other):
        return self.heuristic > other.heuristic or (self.heuristic == other.heuristic and self.puzzle_config >= other.puzzle_config)

    def __repr__(self):
        if self.touch_idx == -1:
            return "0\t%s\n" % (self.puzzle_config)
        return "%s\t%s\n" % (self.getPosition(self.touch_idx), self.puzzle_config)