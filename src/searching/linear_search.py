from .interface import SearchInterface


class LinearSearch(SearchInterface):
    def __init__(self) -> None:
        pass

    def search(self, array, target, callback=None) -> int:

        for i, value in enumerate(array):
            if value == target:
                if callback:
                    callback(array, i, i)
                return i
            if callback:
                callback(array, i, i)
        return -1
    
    def display_bars(self, array, si, ei) -> None:
        from utils import update_search_chart
        update_search_chart(array, si, ei)
    