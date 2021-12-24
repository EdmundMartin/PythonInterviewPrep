

class Solution:
    def defangIPaddr(self, address: str) -> str:
        split_components = address.split('.')
        return '[.]'.join(split_components)
