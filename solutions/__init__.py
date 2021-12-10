from abc import ABC, abstractmethod

from utils.output import Logger

class AbstractSolution(ABC):
    logger: Logger

    def __init__(self) -> None:
        self.logger = Logger()
        super().__init__()

    @abstractmethod
    def solve(self, input: str):
        raise NotImplemented
