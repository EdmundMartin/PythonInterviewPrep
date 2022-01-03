from algoexpert.utils.linked_list import (
    LinkedList,
    linked_list_from_list,
    linked_list_to_python_list,
)


def sum_of_linked_lists(list_one: LinkedList, list_two: LinkedList) -> LinkedList:
    dummy_node = LinkedList(0)
    current_node = dummy_node
    carry = 0
    first_list, second_list = list_one, list_two
    while first_list is not None or second_list is not None or carry != 0:
        first_value = first_list.value if first_list else 0
        second_value = second_list.value if second_list else 0
        sum_values = first_value + second_value + carry
        new_value = sum_values % 10
        new_node = LinkedList(new_value)
        current_node.next = new_node
        current_node = new_node
        carry = sum_values // 10
        first_list = first_list.next if first_list else None
        second_list = second_list.next if second_list else None
    return dummy_node.next


if __name__ == "__main__":
    test_list_one = linked_list_from_list([0, 2, 2])
    test_list_two = linked_list_from_list([1, 1, 1])

    output = sum_of_linked_lists(test_list_one, test_list_two)
    result = linked_list_to_python_list(output)
    assert result == [1, 3, 3]
