"""
    swapping the adjacent elements if they are in the wrong order

    Time complexity - O(n2)
    Space complexity - O(1)
"""

from decorators.decorators import log

@log
def bubble_sort(nums: list[int]) -> list[int]:
    for i in range(len(nums)):
        for j in range(0, len(nums) - i - 1):
            if nums[j] > nums[j + 1]:
                nums[j], nums[j + 1] = nums[j + 1], nums[j]
    return nums

bubble_sort([5,8,9,2,1,999,22]) # [1, 2, 5, 8, 9, 22, 999]