from collections import Counter


def minimumDeletions(s: str) -> int:
    min_deletes = 0
    b_to_rm = 0
    for l in s:
        if l == 'b':
            b_to_rm += 1
        elif b_to_rm:
            min_deletes += 1
            b_to_rm -= 1
    return min_deletes

print(minimumDeletions('aababbab'))