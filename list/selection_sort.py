"""
    Pick the min or max element and move it to the right or left

    Time complexity - O(n2)
    Space complexity - O(1)

"""

from decorators.decorators import log

@log
def selection_sort(nums: list[int]) -> list[int]:
    for i in range(len(nums)):
        min = i
        for j in range(i + 1, len(nums)):
            if nums[j] < nums[min]:
                min = j
        nums[i],nums[min]  = nums[min], nums[i]
    return nums

selection_sort([4, 9, 1, 5, 97, 34]) # [1, 4, 5, 9, 34, 97]