#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import random

PATH_TO_LIST = "list.txt"
PATH_TO_RESULT = "result.txt"

if __name__ == "__main__":
    with open(PATH_TO_LIST, mode="r") as f:
        names = [s.strip() for s in f.readlines()]
    names = [x for x in names if x]
    order = random.sample(names, len(names))
    print("input", names)
    print("result", order)
    with open(PATH_TO_RESULT, mode="w") as f:
        for name in order:
            f.write(name+"\n")
