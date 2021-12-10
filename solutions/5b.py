from itertools import pairwise, chain, takewhile, product
from solutions import AbstractSolution
from operator import ge, itemgetter, lt
from pprint import pprint
from os import linesep
from utils.output import Logger
from collections import Counter


class Solution(AbstractSolution):
    def solve(self, input: str):
        lines = [
            tuple(tuple(map(int, p.split(',')))
                for p in l.split(' -> ')
            ) for l in input.split(linesep)
        ]
        
        points = []
        for l in lines:
            l = sorted(l, key=itemgetter(0))
            ax, ay, bx, by = [*l[0], *l[1]]

            if (ax != bx and ay != by):
                slope = int((by - ay) / (bx - ax))
                points += list(takewhile(lambda x: x[0] <= bx, (z for z in self.increment_point(l[0], slope))))
            else:
                points += (
                    self.line_points(ax, ay, by, True) if (ax == bx)
                    else self.line_points(ay, ax, bx, False)
                )

        seen = set()
        return len(set([p for p in points if p in seen or seen.add(p)]))

    def increment_point(self, point, slope):
        while (True):
            yield point
            x, y = point
            point = (x + 1, y + slope)
        
    def line_points(self, common, a, b, common_is_x):
        line = range(min(a,b), max(a,b) + 1)
        return list(product([common], line) if common_is_x else product(line, [common]))
