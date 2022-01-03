# """
# This is the ImmutableListNode's API interface.
# You should not implement it, or speculate about its implementation.
# """
# class ImmutableListNode:
#     def printValue(self) -> None: # print the value of this node.
#     def getNext(self) -> 'ImmutableListNode': # return the next node.

seen = []


class ImmutableListNode:
    def __init__(self, val: int):
        self.__val = val
        self.__next = None

    def getNext(self):
        return self.__next

    def printValue(self):
        global seen
        seen.append(self.__val)


class Solution:
    def printLinkedListInReverse(self, head: "ImmutableListNode") -> None:
        if head:
            self.printLinkedListInReverse(head.getNext())
            head.printValue()
