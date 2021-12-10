from itertools import pairwise
from solutions import AbstractSolution

class Solution(AbstractSolution):
    def solve(self, input: str):
        l = map(int, input.split("\n"))
        return [x < y for x, y in pairwise(l)].count(1)
