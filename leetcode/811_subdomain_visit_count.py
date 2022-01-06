from typing import List


class Solution:

    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        mapping = dict()
        for cpdomain in cpdomains:
            count, domain = cpdomain.split(' ')
            count = int(count)
            domain_split = domain.split('.')
            i = len(domain_split)
            while i >= 0:
                key = ".".join(domain_split[i:len(domain_split)])
                if key and key not in mapping:
                    mapping[key] = count
                elif key and key in mapping:
                    mapping[key] += count
                i -= 1
        return [f"{value} {key}" for key, value in mapping.items()]


if __name__ == '__main__':
    results = Solution().subdomainVisits(["9001 discuss.leetcode.com"])
    print(results)