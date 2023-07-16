"""
    Binary search is used for search elements from a sorted list

    Time complexity - O(logn)
    Space Complexity - O(1)
"""

from decorators.decorators import log 

# recursive method
@log
def binary_search(nums: list[int], target: int) -> bool:
    if nums == []:
        return False
    mid = len(nums) // 2
    if nums[mid] == target:
        return True
    elif nums[mid] > target:
        return binary_search(nums[:mid], target)
    else:
        return binary_search(nums[mid+1:], target)

# iterative method
@log
def binary_search_loop(nums: list[int], target: int) -> bool:
    s = 0
    e = len(nums) - 1
    while(s <= e):
        mid = (s + e) // 2
        if nums[mid] == target:
            return True
        elif nums[mid] > target:
            e = mid - 1
        else:
            s = mid + 1
    return False



binary_search_loop([x for x in range(10000000)], 999999) # True