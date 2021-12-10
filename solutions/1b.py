from itertools import pairwise
from solutions import AbstractSolution

class Solution(AbstractSolution):
    def solve(self, input: str):
        l = list(map(int, input.split("\n")))
        sets = zip(l[:-2], l[1:-1], l[2:])
        return [x < y for x, y in pairwise(map(sum, sets))].count(1)
