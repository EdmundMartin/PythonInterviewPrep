def sunset_views(buildings, direction):
    # Write your code here.
    if direction == "WEST":
        idx = 0
        iterator = 1
    else:
        idx = len(buildings) - 1
        iterator = -1
    max_height = float("-inf")
    sunset_idxes = []
    while idx >= 0 and idx < len(buildings):
        if buildings[idx] > max_height:
            sunset_idxes.append(idx)
            max_height = max(max_height, buildings[idx])
        idx += iterator
    if direction == "EAST":
        return sunset_idxes[::-1]
    return sunset_idxes


if __name__ == "__main__":
    towers = [3, 5, 4, 4, 3, 1, 3, 2]
    direction = "EAST"
    result = sunset_views(towers, direction)
    print(result)

    towers = [3, 5, 4, 4, 3, 1, 3, 2]
    direction = "WEST"
    result = sunset_views(towers, direction)
    print(result)
