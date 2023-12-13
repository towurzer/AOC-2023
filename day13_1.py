import generalMethods


def check_if_perfect_horizontal(limit: int, field: list[str]) -> bool:
    """checks if the given row is a perfect horizontal mirror of the row above it"""
    i = 0
    while limit-1-i >= 0 and limit + i < len(field):
        if field[limit+i] != field[limit-1-i]:
            return False
        i += 1
    return True


def check_if_perfect_vertical(limit: int, field: list[str]) -> bool:
    """checks if the given column is a perfect vertical mirror of the column to the left of it"""
    column = 0
    while limit-1-column >= 0 and limit + column < len(field[0]):
        for row in field:
            if row[limit+column] != row[limit-1-column]:
                return False
        column += 1
    return True


def main(day) -> None:
    """solution to day 13 part 1"""
    data = [sub_map.split("\n") for sub_map in generalMethods.getInputArray(day, separator="\n\n")]
    final_sum = 0
    for sub_map in data:
        for row_index in range(1, len(sub_map)):
            # if difference between the two rows is just one character flip character and chek if perfect horizontal if yes add row_index*100 to final_sum if not change char back
            if sub_map[row_index] == sub_map[row_index-1] and check_if_perfect_horizontal(row_index, sub_map):
                final_sum += row_index*100
                break

        for column_index in range(1, len(sub_map[0])):
            if check_if_perfect_vertical(column_index, sub_map):
                final_sum += column_index
                break

    print(final_sum)
    # print(final_sum in [34911, 405])


if __name__ == '__main__':
    main(13)
