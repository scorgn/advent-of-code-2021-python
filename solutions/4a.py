from itertools import pairwise, chain, takewhile
from solutions import AbstractSolution
from operator import ge, lt
from pprint import pprint
from os import linesep
from utils.output import Logger


class Solution(AbstractSolution):
    def solve(self, input: str):
        sections = input.split(2*linesep)
        boards = [[l.split() for l in s.split(linesep)] for s in sections[1:]]
        boards += [[list(t) for t in zip(*board)] for board in boards]
        
        for number in sections[0].split(','):
            for board in boards:
                for line in board:
                    if number in line:
                        line.remove(number)
                    if (len(line) == 0):
                        return int(number) * sum(map(int, chain.from_iterable(board)))


