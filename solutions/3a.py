from itertools import pairwise, groupby
from functools import reduce
from solutions import AbstractSolution
from operator import itemgetter, add, sub
from pprint import pprint

class Solution(AbstractSolution):
    def solve(self, input: str):
        lines = input.split("\n")
        half = (len(lines) // 2)
        gamma = int(''.join([str(x.count('1') // half) for x in zip(*lines)]), 2)
        return gamma * ((pow(2, len(lines[0])) - 1) ^ gamma)
