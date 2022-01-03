from algoexpert.utils.linked_list import (
    LinkedList,
    linked_list_to_python_list,
    linked_list_from_list,
)


def remove_kth_node_from_end(head: LinkedList, k: int) -> None:
    counter = 0
    slow = head
    fast = head
    while counter < k:
        fast = fast.next
        counter += 1
    if fast is None:
        head.value = head.next.value
        head.next = head.next.next
        return
    while fast.next:
        fast = fast.next
        slow = slow.next
    slow.next = slow.next.next


if __name__ == "__main__":
    test_list = linked_list_from_list([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    remove_kth_node_from_end(test_list, 3)
    result = linked_list_to_python_list(test_list)
    assert result == [1, 2, 3, 4, 5, 6, 7, 9, 10]
