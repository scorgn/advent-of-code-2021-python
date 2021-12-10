from argparse import ArgumentParser
from os.path import exists
from pprint import pprint
from pathlib import Path
from inspect import getmembers, isclass
from os import listdir, curdir
import sys
from pprint import pprint
from importlib import import_module
from typing import Optional
import solutions
from utils.output import Logger, Color

logger = Logger()

def parse_args() -> dict:
    parser = ArgumentParser()
    parser.add_argument("-a", "--all", dest="run_all",
                        help="Run all solutions", action="store_true")
    parser.add_argument("-l", "--list", dest="list_all",
                        help="List all challenges that have solutions", action="store_true")
    parser.add_argument('challenge', help='Challenge to run')
    return parser.parse_args()

def validate_file(file: str, error_message: Optional[str] = None):
    if not exists(file):
        raise FileNotFoundError('File %s does not exist.' %file)

args = parse_args()
challenge = args.challenge

current_dir = Path(__file__).resolve().parent
completion_file = '%s/solutions/%s.py' %(current_dir, challenge)

if not exists(completion_file):
    raise FileNotFoundError('The solution file for %s does not exist.' %challenge)

input_file = '%s/input/%s.txt' %(current_dir, challenge)
if not exists(input_file):
    input_file = '%s/input/%s.txt' %(current_dir, challenge[0])

if not exists(input_file):
    raise FileNotFoundError('The input file for %s does not exist' %challenge)

example_input_file = '%s/input/example/%s.txt' %(current_dir, challenge)
if not exists(example_input_file):
    example_input_file = '%s/input/example/%s.txt' %(current_dir, challenge[0])

example_answer_input_file = '%s/input/example/answers/%s.txt' %(current_dir, challenge)
if not exists(example_answer_input_file):
    example_answer_input_file = '%s/input/example/answers/%s.txt' %(current_dir, challenge[0])

validate_example = exists(example_input_file) and exists(example_answer_input_file)
if not validate_example:
    logger.warn('The example input and / or answer files for %s does not exist. Answer cannot be validated.' %challenge)

solution_module = import_module('solutions.%s' %challenge)
solution_filter = lambda cls: isclass(cls) and cls != solutions.AbstractSolution and issubclass(cls, solutions.AbstractSolution)
solution_class = next(cls for name, cls in getmembers(solution_module) if solution_filter(cls))
solution = solution_class()

if validate_example:
    solved_example = str(solution.solve(Path(example_input_file).read_text().strip()))
    expected_example_answer = Path(example_answer_input_file).read_text().strip()
    if solved_example != expected_example_answer:
        logger.error('The solution does not produce the correct answer for the example input.')
        logger.warn('Expected example answer: %s' %expected_example_answer)
        logger.warn('Your example answer: %s' %solved_example)
    else:
        logger.success('Your solution produces the correct answer for the example input!')

answer = solution_class().solve(Path(input_file).read_text().strip())
logger.white('Your answer: %s' %answer)
