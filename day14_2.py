import generalMethods


class Rock:
    def __init__(self, row: int, column: int):
        self.row = row
        self.column = column
        # self.previous_pos = (row, column)

    def slide_north(self) -> None:
        """slides the rock to the north"""
        global data
        data[self.row] = generalMethods.replaceCharacterInString(data[self.row], self.column, ".")
        while self.row > 0 and data[self.row - 1][self.column] == ".":
            self.row -= 1
        data[self.row] = generalMethods.replaceCharacterInString(data[self.row], self.column, "O")

    def slide_south(self) -> None:
        """slides the rock to the south"""
        global data
        data[self.row] = generalMethods.replaceCharacterInString(data[self.row], self.column, ".")
        while self.row < len(data) - 1 and data[self.row + 1][self.column] == ".":
            self.row += 1
        data[self.row] = generalMethods.replaceCharacterInString(data[self.row], self.column, "O")

    def slide_east(self) -> None:
        """slides the rock to the east"""
        global data
        data[self.row] = generalMethods.replaceCharacterInString(data[self.row], self.column, ".")
        while self.column < len(data[self.row]) - 1 and data[self.row][self.column + 1] == ".":
            self.column += 1
        data[self.row] = generalMethods.replaceCharacterInString(data[self.row], self.column, "O")

    def slide_west(self) -> None:
        """slides the rock to the west"""
        global data
        data[self.row] = generalMethods.replaceCharacterInString(data[self.row], self.column, ".")
        while self.column > 0 and data[self.row][self.column - 1] == ".":
            self.column -= 1
        data[self.row] = generalMethods.replaceCharacterInString(data[self.row], self.column, "O")

    def evaluate_score(self) -> int:
        """evaluates the score of the rock"""
        global data
        return len(data) - self.row


def find_rocks(data: list) -> list[Rock]:
    """finds all rocks in the data and returns them as a list of rock objects"""
    rocks = []
    for row_index in range(len(data)):
        for c_index in range(len(data[row_index])):
            if data[row_index][c_index] == "O":
                rocks.append(Rock(row_index, c_index))
    return rocks


def main(day, tilts: int) -> None:
    global data
    data = generalMethods.getInputArray(day)
    rocks = find_rocks(data)

    # tilt data
    previous_data = [data.copy()]
    for _ in range(tilts):
        rocks.sort(key=lambda x: x.row)
        for rock in rocks:
            rock.slide_north()
        rocks.sort(key=lambda x: x.column)
        for rock in rocks:
            rock.slide_west()
        rocks.sort(key=lambda x: x.row, reverse=True)
        for rock in rocks:
            rock.slide_south()
        rocks.sort(key=lambda x: x.column, reverse=True)
        for rock in rocks:
            rock.slide_east()
        previous_data.append(data.copy())
        if previous_data.count(data) > 1:
            # there is a loop in the data,
            # therefore we can skip the rest of the tilts and just calculate the final score
            loop_length = previous_data[previous_data.index(data) + 1:].index(data) + 1
            loop_start = previous_data.index(data)
            data = previous_data[loop_start + (tilts - loop_start) % loop_length]
            break

    rocks = find_rocks(data)
    final_score = 0
    for rock in rocks:
        final_score += rock.evaluate_score()
    print(final_score)


data = []
if __name__ == '__main__':
    main(14, tilts=1_000_000_000)
