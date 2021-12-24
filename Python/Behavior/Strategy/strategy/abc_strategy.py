from abc import ABC, abstractmethod

class AbcStrategy(ABC):

    @abstractmethod
    def calculate(self, order):
        """Calculate shipping cost"""
        pass