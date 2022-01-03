from typing import List

# TODO - Comeback to


def non_constructible_change(coins: List[int]) -> int:
    coins.sort()
    current_change_created = 0
    for coin in coins:
        if coin > current_change_created + 1:
            return current_change_created + 1
        current_change_created += coin
    return current_change_created + 1


if __name__ == "__main__":
    coins = [5, 7, 1, 1, 2, 3, 22]
    result = non_constructible_change(coins)
    assert result == 20
