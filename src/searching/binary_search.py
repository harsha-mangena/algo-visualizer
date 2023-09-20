from .interface import SearchInterface

class BinarySearch(SearchInterface):

    def __init__(self) -> None:
        pass
    
    def search(self, array, target):
        low, high = 0, len(array) - 1

        while low <= high:
            mid = (low + high) // 2
            if array[mid] == target:
                return mid
            elif array[mid] < target:
                low = mid + 1
            else:
                high = mid - 1

        return -1
    
    def display_content(self) -> None:
        pass
        