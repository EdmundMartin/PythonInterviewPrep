from typing import List


class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        mapping = {}
        for idx, val in enumerate(list1):
            mapping[val] = idx

        min_value = float('inf')
        results = set()
        for idx, value in enumerate(list2):
            current_sum = idx + mapping.get(value, float('inf'))
            if current_sum < min_value:
                results = {value}
                min_value = current_sum
            if current_sum == min_value:
                results.add(value)
        return list(results)


if __name__ == '__main__':
    first_list = ["Shogun", "Tapioca Express", "Burger King", "KFC"]
    second_list = ["Piatti", "The Grill at Torrey Pines", "Hungry Hunter Steakhouse", "Shogun"]

    result = Solution().findRestaurant(first_list, second_list)
    assert result == ["Shogun"]
