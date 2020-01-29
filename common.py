# This method takes a file name as input and returns a list with the puzzle configurations
def getInput(inputFile):
    inputList = [];
    with open(inputFile) as file:
        for line in file:
            puzzle_config = line.split();
            if len(puzzle_config) != 4:
                raise Exception("Incorrect input format. Verify file: " + inputFile);
            inputList.append(line.split());
    return inputList;

for element in getInput("input.txt"):
    print(element);
