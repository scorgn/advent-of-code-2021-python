from itertools import pairwise, groupby
from functools import reduce
from solutions import AbstractSolution
from operator import itemgetter, add, sub
from pprint import pprint


class Solution(AbstractSolution):
    def solve(self, input: str):
        # a[0] - depth 
        # a[1] - horizontal
        # a[2] - aim
        # b[0] - direction
        # b[1] - amount
        position = reduce(lambda a, b: (
            (a[0] + (int(b[1]) * a[2]), a[1] + int(b[1]), a[2]) if b[0] == 'forward'
            else (a[0], a[1], a[2] + int(b[1]) if b[0] == 'down' else a[2] - int(b[1]))
        ), [x.split() for x in input.split("\n")], (0,0,0))

        return position[0] * position[1]
