"""
    Sorting the list using divide and conquere technique in place

    Time complexity - O(n2) (worst case), O(nlogn) (average case)
    Space complexity - O(1)

"""

from decorators.decorators import log

@log
def quick_sort(nums: list[int], start: int, end: int) -> list[int]:
    if (end - start) <= 1:
        return nums
    pivot, lower, upper = start, start + 1, start + 1
    for x in range(start + 1, end):
        if nums[x] > nums[pivot]:
            upper += 1
        else:
            nums[x], nums[lower] = nums[lower], nums[x]
            upper, lower = upper + 1, lower + 1
    nums[pivot], nums[lower - 1] = nums[lower - 1], nums[pivot]
    lower -= 1
    quick_sort(nums, start, lower)
    quick_sort(nums, lower + 1, end)
    return nums


quick_sort([7,1,4,3,6], 0, 5) # [1, 3, 4, 6, 7]
