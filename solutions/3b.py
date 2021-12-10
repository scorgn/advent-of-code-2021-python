from solutions import AbstractSolution
from operator import ge, lt

class Solution(AbstractSolution):
    def solve(self, input: str):
        originallines = input.split("\n")
        col_indexes = range(0, len(originallines[0]))
        rating = 1

        for compare in [ge, lt]:
            lines = originallines.copy()
            for col in col_indexes:
                half = len(lines) / 2
                count_1 = list(zip(*lines))[col].count("1")
                should_keep_1 = compare(count_1, half)
                keep = str(int(should_keep_1))
                lines = [line for line in lines if line[col] == keep]
                if len(lines) == 1:
                    break

            rating *= int(''.join(lines[0]), 2)
        
        return rating

