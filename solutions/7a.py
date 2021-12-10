from functools import reduce
from typing import Counter
from solutions import AbstractSolution
from pprint import pprint

class Solution(AbstractSolution):
    def solve(self, input: str):
        starting_points = list(map(int, input.split(',')))
        potential_meeting_points = range(min(starting_points), max(starting_points) + 1)
        return min([reduce(lambda carry, new: carry + abs(i - new), starting_points, 0) for i in potential_meeting_points])
