from itertools import pairwise, chain, takewhile
from solutions import AbstractSolution
from operator import ge, lt
from pprint import pprint
from os import linesep
from utils.output import Logger


class Solution(AbstractSolution):
    def solve(self, input: str):
        sections = input.split(2*linesep)
        numbers = sections[0].split(',')
        horizontal = [[l.split() for l in s.split(linesep)] for s in sections[1:]]
        vertical = [[list(t) for t in zip(*board)] for board in horizontal]
        boards = list(zip(horizontal, vertical))
    
        for number in numbers:
            for k, v in enumerate(boards):
                if v is None: continue
                for board in v:
                    for line in board:
                        if number in line:
                            line.remove(number)
                        if (len(line) > 0):
                            continue
                        if (len(boards) == boards.count(None) + 1):
                            return int(number) * sum(map(int, chain.from_iterable(board)))
                        boards[k] = None
                        break

