# Task: Search in Rotated Sorted Array II
#
# There is an integer array 'nums' sorted in non-decreasing order.
# Before being passed to your function, 'nums' is rotated at an unknown pivot
# index 'k' (0 <= k < nums.length), so the array becomes:
# [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]].
#
# Given the rotated array and a target, return 'true' if the target exists,
# otherwise return 'false'.
# The time complexity should be minimized as much as possible.
#
#
# Задача: Поиск в Повернутом Отсортированном Массиве II
#
# Дан целочисленный массив 'nums', отсортированный в неубывающем порядке.
# Перед передачей в функцию, массив 'nums' поворачивается вокруг неизвестного
# индекса 'k' (0 <= k < nums.length). Итоговый массив становится:
# [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]].
#
# Дано число 'target'. Верните 'true', если оно присутствует в массиве,
# иначе верните 'false'. Ваша задача минимизировать количество операций.
#
#
# Example 1:
# Input: nums = [2,5,6,0,0,1,2], target = 0
# Output: true
#
# Example 2:
# Input: nums = [2,5,6,0,0,1,2], target = 3
# Output: false


from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> bool:  # noqa C901
        if not nums:
            return False
        if len(nums) == 1:
            return nums[0] == target

        first, last = 0, len(nums) - 1

        while first <= last:
            mid = first + (last - first) // 2

            if nums[mid] == target:
                return True

            if nums[first] == nums[mid]:
                first += 1
                continue

            if nums[first] < nums[mid]:
                if nums[first] <= target <= nums[mid]:
                    last = mid - 1
                else:
                    first = mid + 1
            else:
                if nums[mid] <= target <= nums[last]:
                    first = mid + 1
                else:
                    last = mid - 1

        return False

# Бинарный поиск с дубликатами.
