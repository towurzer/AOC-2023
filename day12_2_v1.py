import time
import day12_1
import generalMethods


def main(day) -> None:
    st2 = time.time()
    data = generalMethods.getInputArray(day)
    possible_arrangements_sum = 0
    for row_index in range(len(data)):
        damaged_record = data[row_index][:data[row_index].index(" ")]*5
        damaged_group_lengths = list(map(int, data[row_index][data[row_index].index(" ")+1:].split(",")))*5
        possible_arrangements_sum += day12_1.find_possible_arrangements(damaged_record, damaged_group_lengths)
        print(f"finished row: {row_index+1}/{len(data)} (after {time.time()-st2} seconds)")

    print("\n\n\n\n\n")
    print(f"Solution: {possible_arrangements_sum}")
    # print(possible_arrangements_sum in [525152])


if __name__ == '__main__':
    st = time.time()
    main(12)
    print(f"Program took {round(time.time() - st, 2)} seconds to run")
