# https://leetcode.com/problems/sort-colors/

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        def quick_sort(a: list[int]) -> list[int]:
            if not a:
                return []
            if len(a) == 1:
                return a

            pivot = a[0]

            left = [x for x in a if x < pivot]
            middle = [x for x in a if x == pivot]
            right = [x for x in a if x > pivot]

            return quick_sort(left) + middle + quick_sort(right)

        sorted_nums = quick_sort(nums)
        nums[:] = sorted_nums
