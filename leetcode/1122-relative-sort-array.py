from collections import Counter

class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        # Collect numbers in arr2
        arr1_counter = Counter(arr1)
        result = []
        for num in arr2:
            result += [num] * arr1_counter.pop(num)

        # Collect numbers not in arr2
        rest = list(arr1_counter.keys())
        rest.sort()
        for num in rest:
            result += [num] * arr1_counter.pop(num)
        return result
