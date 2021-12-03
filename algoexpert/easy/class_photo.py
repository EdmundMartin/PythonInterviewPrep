from typing import List


def class_photo(red_heights: List[int], blue_heights: List[int]) -> bool:
    red_heights.sort(reverse=True)
    blue_heights.sort(reverse=True)
    if red_heights[0] > blue_heights[0]:
        back_row, front_row = red_heights, blue_heights
    else:
        back_row, front_row = blue_heights, red_heights
    for back, front in zip(back_row, front_row):
        if back <= front:
            return False
    return True


if __name__ == '__main__':
    reds = [5, 8, 1, 3, 4]
    blues = [6, 9, 2, 4, 5]

    result = class_photo(reds, blues)
    assert result is True
