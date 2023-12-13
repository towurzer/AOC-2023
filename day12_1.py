import time
import generalMethods


def check_if_arrangement_is_valid(row: str, groups: list[int]) -> bool:
    fail_groups = []
    current_fail_counter = 0
    for char in row:
        if char == "#":
            current_fail_counter += 1
        elif char == ".":
            if current_fail_counter > 0:
                fail_groups.append(current_fail_counter)
                if len(fail_groups) > len(groups) or fail_groups[-1] != groups[len(fail_groups)-1]:
                    return False
                current_fail_counter = 0
        elif char == "?":
            exit("ERROR: ? in row")
        else:
            exit("ERROR: unknown char in row")
    if current_fail_counter > 0:
        fail_groups.append(current_fail_counter)

    return fail_groups == groups


def find_possible_arrangements(row: str, groups: list[int]) -> int:
    possible_arrangements = 0
    for char_index in range(len(row)):
        if row[char_index] == "?":
            possible_arrangements += find_possible_arrangements(
                generalMethods.replaceCharacterInString(row, char_index, "#"), groups)
            possible_arrangements += find_possible_arrangements(
                generalMethods.replaceCharacterInString(row, char_index, "."), groups)
            break
    if "?" not in row:
        if check_if_arrangement_is_valid(row, groups):
            return 1
        else:
            return 0
    else:
        return possible_arrangements


def main(day) -> None:
    data = generalMethods.getInputArray(day)
    possible_arrangements_sum = 0
    for row_index in range(len(data)):
        damaged_record = data[row_index][:data[row_index].index(" ")]
        damaged_group_lengths = list(map(int, data[row_index][data[row_index].index(" ")+1:].split(",")))
        possible_arrangements_sum += find_possible_arrangements(damaged_record, damaged_group_lengths)

    print(possible_arrangements_sum)
    # print(possible_arrangements_sum in [21, 8180])


if __name__ == '__main__':
    st = time.time()
    main(12)
    print(f"Program took {round(time.time() - st, 2)} seconds to run")
