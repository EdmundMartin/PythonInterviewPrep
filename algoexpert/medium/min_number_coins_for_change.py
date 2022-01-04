from typing import List


def minimum_number_of_coins(n: int, denoms: List[int]) -> int:
    num_of_coins = [float('inf')] * (n + 1)
    num_of_coins[0] = 0
    for denom in denoms:
        for amount in range(len(num_of_coins)):
            if denom <= amount:
                num_of_coins[amount] = min(num_of_coins[amount], 1 + num_of_coins[amount - denom])
    return num_of_coins[n] if num_of_coins[n] != float('inf') else -1


if __name__ == '__main__':
    res = minimum_number_of_coins(6, [1, 2, 4])
    print(res)
