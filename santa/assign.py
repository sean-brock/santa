import random
from typing import List
import sys

def eprint(*args, **kwargs):
    print(*args, file=sys.stderr, **kwargs)

def shuffle(list_in: list) -> list:
    shuff = []
    li = list_in.copy()
    while len(li) > 0:
        i = random.randint(0, len(li) - 1)
        shuff.append(li.pop(i))
    return shuff


def santa(names: List[str]):
    pairs = {}

    shuffled = shuffle(names)
    for i in range(len(shuffled)):
        j = i + 1 if i < len(shuffled) - 1 else 0
        pairs[shuffled[i]] = shuffled[j]
    return pairs


def validate(pairs: dict) -> bool:
    keys = set()
    vals = set()
    for x, y in pairs.items():
        if x == y:
            eprint("Key value pair are the same item.")
            return False
        keys.add(x)
        vals.add(y)

    # check duplicate key/val
    expected_items = len(pairs)
    if expected_items != len(keys):
        eprint("Duplicate keys found in output.")
        return False
    if expected_items != len(vals):
        eprint("Duplicate values found in output.")
        return False

    # Check vals not in keys
    if vals != keys:
        eprint("Unique values present not found in keys.")
        return False


    return True


