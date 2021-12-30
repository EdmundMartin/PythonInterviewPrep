from typing import List


def is_valid_part(string: str):
    int_repr = int(string)
    if int_repr > 255 or int_repr < 0:
        return False

    # Checks for leading zeros
    return len(string) == len(str(int_repr))


def valid_ip_addresses(string: str) -> List[str]:
    found = []

    for idx in range(1, min(len(string), 4)):
        current_ip_address_parts = ['', '', '', '']

        current_ip_address_parts[0] = string[:idx]
        if not is_valid_part(current_ip_address_parts[0]):
            continue
        for second_idx in range(idx + 1, idx + min(len(string) - idx, 4)):
            current_ip_address_parts[1] = string[idx:second_idx]
            if not is_valid_part(current_ip_address_parts[1]):
                continue
            for third_idx in range(second_idx + 1, second_idx + min(len(string) - second_idx, 4)):
                current_ip_address_parts[2] = string[second_idx: third_idx]
                current_ip_address_parts[3] = string[third_idx:]

                if is_valid_part(current_ip_address_parts[2]) and is_valid_part(current_ip_address_parts[3]):
                    found.append('.'.join(current_ip_address_parts))
    return found
