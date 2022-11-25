import argparse
import random
from typing import List


def shuffle(list_in: list) -> list:
    shuff = []
    li = list_in.copy()
    while len(li) > 0:
        i = random.randint(0, len(li) - 1)
        shuff.append(li.pop(i))
    return shuff


def santa(names: List[str]):
    pairs = {}
    success = False
    iters = 0

    def generate(pairs: dict) -> bool:
        shuffled = shuffle(names)
        for name in names:
            count = 0
            while name == shuffled[count]:
                if len(shuffled) == 1:
                    return False
                count += 1
                if count >= len(shuffled):
                    count = 0
            pairs[name] = shuffled.pop(count)
        return True

    done = False
    while not done:
        done = generate(pairs)
        iters += 1
    print(f"Solved in {iters} iterations.")
    return pairs


def validate(pairs: dict) -> bool:
    for x, y in pairs.items():
        if x == y:
            return False
    return True


