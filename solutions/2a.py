from itertools import pairwise, groupby
from solutions import AbstractSolution
from operator import itemgetter
from pprint import pprint


class Solution(AbstractSolution):
    def solve(self, input: str):
        lines = [x.split() for x in sorted(input.split("\n"))]
        grouped = groupby(lines, itemgetter(0))
        amounts = {x: sum([int(q) for _, q in y]) for x, y in grouped}
        return (amounts['down'] - amounts['up']) * amounts['forward']
