# coding: utf-8
def advent_1a(depths: list) -> int:
    num_increases = 0
    for curr_depth, next_depth in zip(depths, depths[1:]):
        print(curr_depth, next_depth)
        if next_depth > curr_depth:
            num_increases += 1
    return num_increases


def advent_1b(depths: list) -> int:
    # first create the 3 measurement groups
    three_measurement_group_sums = []
    for index, val in enumerate(depths):
        three_m_group = depths[index : index + 3]
        if len(three_m_group) < 3:
            break
        three_measurement_group_sums.append(sum(three_m_group))
    return advent_1a(three_measurement_group_sums)


input_data = [199, 200, 208, 210, 200, 207, 240, 269, 260, 263]
assert (advent_1a(input_data)) == 7
assert (advent_1b(input_data)) == 5
