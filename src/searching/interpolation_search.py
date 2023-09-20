from .interface import SearchInterface

class InterpolationSearch(SearchInterface):
    def __init__(self) -> None:
        pass 

    def search(self, array, target) -> int:
        low, high = 0, len(array) - 1

        while low <= high and target >= array[low] and target <= array[high]:
            # Estimate the position
            position = low + int(((target - array[low]) * (high - low)) / (array[high] - array[low]))

            if array[position] == target:
                return position

            if array[position] < target:
                low = position + 1
            else:
                high = position - 1

        return -1

    def display_content(self) -> None:
        pass 