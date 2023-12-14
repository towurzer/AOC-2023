import generalMethods


class Rock:
    def __init__(self, row: int, column: int):
        self.row = row
        self. column = column

    def slide(self) -> None:
        """slides the rock one step down"""
        global data
        data[self.row] = generalMethods.replaceCharacterInString(data[self.row], self.column, ".")
        while self.row > 0 and data[self.row-1][self.column] == ".":
            self.row -= 1
        data[self.row] = generalMethods.replaceCharacterInString(data[self.row], self.column, "O")

    def evaluate_score(self) -> int:
        """evaluates the score of the rock"""
        global data
        return len(data) - self.row


def main(day) -> None:
    global data
    data = generalMethods.getInputArray(day)
    rocks = []
    # find all rocks and store them in a list of rock objects
    for row_index in range(len(data)):
        for c_index in range(len(data[row_index])):
            if data[row_index][c_index] == "O":
                rocks.append(Rock(row_index, c_index))

    # tilt data north, let the rocks slide and evaluate the final score
    final_score = 0
    for rock in rocks:
        rock.slide()
        final_score += rock.evaluate_score()

    print(final_score)


data = []
if __name__ == '__main__':
    main(14)
