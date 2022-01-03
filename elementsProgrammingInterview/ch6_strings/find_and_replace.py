"""
Consider the following two rules that are to be applied to an array of characters.

* Replace each 'a' by two 'd's
* Delete each entry containing a 'b'
"""
from typing import List


def replace_and_remove(size: int, s: List[str]) -> int:
    # Forward iterate remove 'b's and count the number of a's
    write_idx, a_count = 0, 0
    for idx in range(size):
        if s[idx] != "b":
            s[write_idx] = s[idx]
            write_idx += 1
        if s[idx] == "a":
            a_count += 1

    curr_idx = write_idx - 1
    write_idx += a_count - 1
    final_size = write_idx + 1
    while curr_idx >= 0:
        if s[curr_idx] == "a":
            s[write_idx - 1 : write_idx + 1] = "dd"
            write_idx -= 2
        else:
            s[write_idx] = s[curr_idx]
            write_idx -= 1
        curr_idx -= 1
    return final_size
