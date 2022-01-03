from typing import List


def tandem_bicycle(
    red_shirt_speeds: List[int], blue_shirt_speeds: List[int], fastest: bool
) -> int:
    red_shirt_speeds.sort()
    blue_shirt_speeds.sort()

    if not fastest:
        red_shirt_speeds = red_shirt_speeds[::-1]

    total_speed = 0
    for idx, _ in enumerate(red_shirt_speeds):
        first_rider = red_shirt_speeds[idx]
        second_rider = blue_shirt_speeds[len(blue_shirt_speeds) - idx - 1]
        total_speed += max(first_rider, second_rider)

    return total_speed


if __name__ == "__main__":
    red_test = [5, 5, 3, 9, 2]
    blue_test = [3, 6, 7, 2, 1]
    result = tandem_bicycle(red_test, blue_test, True)
    assert result == 32
