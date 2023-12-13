import generalMethods


def check_if_near_perfect_horizontal(limit: int, field: list[str]) -> bool:
    """checks if the given row is a horizontal mirror with the row above it with exactly one mistake"""
    i = 0
    fixed_fail = False
    while limit-1-i >= 0 and limit + i < len(field):
        if field[limit+i] != field[limit-1-i]:
            if fixed_fail:
                return False
            for c_index in range(len(field[limit+i])):
                if field[limit+i][c_index] != field[limit-1-i][c_index]:
                    if fixed_fail:
                        return False
                    fixed_fail = True
        i += 1
    return fixed_fail


def check_if_near_perfect_vertical(limit: int, field: list[str]) -> bool:
    """checks if the given column is a vertical mirror with the column to the left of it with exactly one mistake"""
    column = 0
    fixed_fail = False
    while limit-1-column >= 0 and limit + column < len(field[0]):
        for row in field:
            if row[limit+column] != row[limit-1-column]:
                if fixed_fail:
                    return False
                for r_index in range(len(field)):
                    if field[r_index][limit+column] != field[r_index][limit-1-column]:
                        if fixed_fail:
                            return False
                        fixed_fail = True
        column += 1
    return fixed_fail


def main(day) -> None:
    """solution to day 13 part 2"""
    data = [sub_map.split("\n") for sub_map in generalMethods.getInputArray(day, separator="\n\n")]
    final_sum = 0
    for sub_map in data:
        for row_index in range(1, len(sub_map)):
            if check_if_near_perfect_horizontal(row_index, sub_map):
                final_sum += row_index*100
                break

        for column_index in range(1, len(sub_map[0])):
            if check_if_near_perfect_vertical(column_index, sub_map):
                final_sum += column_index
                break

    print(final_sum)
    # print(final_sum in [33183, 400]


if __name__ == '__main__':
    main(13)
