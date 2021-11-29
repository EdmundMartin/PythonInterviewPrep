from typing import List
from collections import defaultdict


def tournament_winner(competitions: List[List[str]], results: List[int]):
    scores = defaultdict(int)
    for comp, result in zip(competitions, results):
        if result == 1:
            idx = 0
        else:
            idx = 1
        scores[comp[idx]] += 3
    return max(scores, key=scores.get)


if __name__ == '__main__':
    test_competitions = [
        ["HTML", "C#"],
        ["C#", "Python"],
        ["Python", "HTML"]
    ]
    test_results = [0, 0, 1]
    result = tournament_winner(test_competitions, test_results)
    assert result == "Python"
