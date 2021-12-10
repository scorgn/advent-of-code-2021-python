from functools import reduce
from itertools import chain
from typing import Counter
from solutions import AbstractSolution
from pprint import pprint

class Solution(AbstractSolution):
    def solve(self, input: str):
        words = list(map(lambda line: line.split('|').pop().split(), input.split("\n")))
        return len(list(filter(lambda x: len(x) in [3,7,4,2], chain(*words))))
