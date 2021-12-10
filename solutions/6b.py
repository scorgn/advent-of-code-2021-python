from functools import reduce
from typing import Counter
from solutions import AbstractSolution
from pprint import pprint

class Solution(AbstractSolution):
    def solve(self, input: str):
        starting_points = list(map(int, input.split(',')))
        range_half_of_days = range(0, 128)
        ones_to_multiply = {}
        for i in range(0,9):
            amounts = {}
            numbers = [i]
            for day in range_half_of_days:
                newNumbers = 0
                for k, number in enumerate(numbers):
                    if number > 0:
                        numbers[k] -= 1
                    else:
                        numbers[k] = 6
                        newNumbers += 1
                day += 1
                numbers += [8] * newNumbers
                amounts[day] = len(numbers)

            ones_to_multiply[i] = Counter(numbers)
        
        return sum([
            sum([
                sum(ones_to_multiply[l].values()) * ones_to_multiply[x][l] for l in ones_to_multiply[x]
            ]) for x in starting_points
        ])
