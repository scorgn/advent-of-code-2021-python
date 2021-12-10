from functools import reduce
from typing import Counter
from solutions import AbstractSolution
from pprint import pprint

class Solution(AbstractSolution):
    def solve(self, input: str):
        crabs = list(map(int, input.split(',')))
        available = range(min(crabs), max(crabs) + 1)
        return int(min([reduce(lambda carry, new: carry + self.nth_tri_num(abs(i - new)), crabs, 0) for i in available]))

    def nth_tri_num(self, n):
        return (pow(n, 2) + n) / 2
