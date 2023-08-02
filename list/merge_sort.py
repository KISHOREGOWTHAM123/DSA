"""
    Sorting the list using divide and conquere technique

    Time complexity - O(nlogn)
    Space complexity - O(n)

"""

from decorators.decorators import log

def merge(arr1: list[int], arr2: list[int]) -> list[int]:
    m, n = len(arr1), len(arr2)
    arr3, i, j, k = [], 0, 0, 0
    while k < m + n:
        if i == m:
            arr3 += arr2[j:]
            k += n - j
        elif j == n:
            arr3 += arr1[i:]
            k += m - i
        elif arr1[i] < arr2[j]:
            arr3.append(arr1[i])
            i += 1
            k += 1
        else:
            arr3.append(arr2[j])
            j += 1
            k += 1
    return arr3

@log
def merge_sort(nums: list[int]) -> list[int]:
    n: int = len(nums)
    if n <= 1:
        return nums
    left_arr = merge_sort(nums[:n//2])
    print('left -> ',left_arr)
    right_arr = merge_sort(nums[n//2:])
    print('right -> ',right_arr)
    return merge(left_arr, right_arr)


merge_sort([4,7,3,1,78, 37, 41]) # [1, 3, 4, 7, 37, 41, 78]