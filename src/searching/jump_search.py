from .interface import SearchInterface

class JumpSearch(SearchInterface):
    def __init__(self) -> None:
        pass

    def search(self, array, target) -> int:
        length = len(array)
        jump = int(array.sqrt(length))
        prev, curr = 0, 0

        # Jump the steps until we find a block that contains the target or go out of bounds
        while curr < length and array[curr] < target:
            prev = curr
            curr += jump

        # Perform linear search in the block
        for index in range(prev, min(curr, length)):
            if array[index] == target:
                return index

        return -1

    def display_content(self) -> None:
        pass


        
