from typing import List


class Solution:
    def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
        rules = {"type": 0, "color": 1, "name": 2}
        rule_idx = rules[ruleKey]
        count = 0
        for item in items:
            if item[rule_idx] == ruleValue:
                count += 1
        return count
