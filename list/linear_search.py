"""
    Linear search is used to search a element from the list from left to right
    or vice versa.

    Time complexity - O(n)
    Space complexity - O(1)

"""

from decorators.decorators import log 

@log
def linear_search(nums: list[int], target: int) -> bool:
    for element in nums:
        if element == target:
            return True
    return False

linear_search([x for x in range(10000000)], 999999) # True