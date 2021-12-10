from functools import reduce
from solutions import AbstractSolution


class Solution(AbstractSolution):
    def solve(self, input: str):
        starting_points = list(map(int, input.split(',')))
        amounts = {}
        numbers = [0]
        for day in range(0, 80):
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
        
        return reduce(lambda carry, new: carry + amounts[80 - new], starting_points, 0)
