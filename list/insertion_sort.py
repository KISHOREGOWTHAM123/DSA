"""
    Pick a element and insert it in a sorted list

    Time complexity -
    Space complexity - 
"""

from decorators.decorators import log

@log
def insertion_sort(nums: list[int]) -> list[int]:
    for i in range(len(nums)):
        j = i
        while j > 0 and nums[j] < nums[j - 1]:
            nums[j], nums[j - 1] = nums[j - 1], nums[j]
            j -= 1
    return nums

insertion_sort([34, 36, 12, 3, 67]) # [3, 12, 34, 36, 67]
