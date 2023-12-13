import time
import generalMethods


def evaluate_possible_arrangements(row: str, groups: list[int]) -> int:
    fail_groups = []
    current_fail_counter = 0
    possible_arrangements = 0
    for char_index in range(len(row)):
        char = row[char_index]
        if (len(fail_groups) > len(groups) or
                len(fail_groups) < len(groups) and current_fail_counter > groups[len(fail_groups)] or
            len(fail_groups) > 0 and fail_groups[-1] != groups[len(fail_groups) - 1]):
            break

        if char == "#":
            current_fail_counter += 1
        elif char == ".":
            if current_fail_counter > 0:
                fail_groups.append(current_fail_counter)
                current_fail_counter = 0
        elif char == "?":
            fail_groups = []
            possible_arrangements += evaluate_possible_arrangements(
                generalMethods.replaceCharacterInString(row, char_index, "#"), groups)
            possible_arrangements += evaluate_possible_arrangements(
                generalMethods.replaceCharacterInString(row, char_index, "."), groups)
            break

    if current_fail_counter > 0:
        fail_groups.append(current_fail_counter)

    if fail_groups == groups:
        possible_arrangements += 1

    return possible_arrangements




def main(day) -> None:
    st2 = time.time()
    data = generalMethods.getInputArray(day)
    possible_arrangements_sum = 0
    for row_index in range(len(data)):
        damaged_record = data[row_index][:data[row_index].index(" ")]
        damaged_record += "?"
        damaged_record *= 5
        damaged_record = damaged_record[:len(damaged_record)-1]
        damaged_group_lengths = list(map(int, data[row_index][data[row_index].index(" ")+1:].split(",")))*5
        possible_arrangements_sum += evaluate_possible_arrangements(damaged_record, damaged_group_lengths)
        print(f"finished row: {row_index+1}/{len(data)} (after {time.time()-st2} seconds)")

    print()
    print(f"Solution: {possible_arrangements_sum}")
    # print(possible_arrangements_sum in [525152])


if __name__ == '__main__':
    st = time.time()
    main(12)
    print(f"Program took {round(time.time() - st, 2)} seconds to run")
