from abc import ABC, abstractmethod

class IDice(ABC):

    @abstractmethod
    def RollDice(self):
        pass