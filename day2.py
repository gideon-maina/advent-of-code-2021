def advent_2a(course: list) -> int:
    horizontal_pos, depth = 0, 0
    for direction in course:
        action, steps = direction.split()
        steps = int(steps)
        if action == "forward":
            horizontal_pos += steps
        elif action == "down":
            depth += steps
        elif action == "up":
            depth -= steps
    print(f"Horiz: {horizontal_pos}, Depth: {depth}, Product: {horizontal_pos * depth}")
    return horizontal_pos * depth


def advent_2b(course: list) -> int:
    horizontal_pos, depth, aim = 0, 0, 0
    for direction in course:
        action, steps = direction.split()
        steps = int(steps)
        if action == "forward":
            horizontal_pos += steps
            # print(f"\t>>horiz increase by {steps}")
            if aim > 0:
                depth += aim * steps
                # print(f"\t\t>>depth increase by {aim * steps}")
        elif action == "down":
            aim += steps
            # print(f"\t\t\t>>aim increase by {steps}")
        elif action == "up":
            # depth -= steps
            # print(f"\t\t>>depth decrease by {steps}")
            aim -= steps
            # print(f"\t\t\t>>aim decrease by {steps}")
        # print("---"*20)
    print(f"Horiz: {horizontal_pos}, Depth: {depth}, Product: {horizontal_pos * depth}")
    return horizontal_pos * depth


input_data = ["forward 5", "down 5", "forward 8", "up 3", "down 8", "forward 2"]
assert (advent_2a(input_data)) == 150
assert (advent_2b(input_data)) == 900

# Use this bash command to convert the copied input from the website to items of the list you'll use 
# pbpaste - this pastes your copied input
# pbpaste | awk -v FS="\n" -v OFS="'" '{print "",$1, ""}' | paste -sd, -
