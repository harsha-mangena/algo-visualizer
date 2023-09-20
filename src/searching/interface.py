from abc import ABC, abstractmethod

class SearchInterface(ABC):

    @abstractmethod
    def search(self, array, target, callback)-> int:
        pass

    @abstractmethod
    def display_bars(self) -> None:
        pass