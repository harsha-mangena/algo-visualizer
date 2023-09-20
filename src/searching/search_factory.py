import constants as c
from .binary_search import BinarySearch
from .linear_search import LinearSearch
from .jump_search import JumpSearch
from .interpolation_search import InterpolationSearch

class SearchFactory:
    @staticmethod
    def get_object(algorithm_name: str) -> object:
        if algorithm_name == c.BINARY_SEARCH:
            return BinarySearch()
        elif algorithm_name == c.INTERPOLATION_SEARCH:
            return InterpolationSearch()
        elif algorithm_name == c.JUMP_SEARCH:
            return JumpSearch()
        elif algorithm_name == c.LINEAR_SEARCH:
            return LinearSearch()
