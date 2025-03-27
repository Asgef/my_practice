# Задача: "Контейнер с Максимальным Объемом"
# Дано целочисленный массив height длиной n. Существует n вертикальных линий,
# такие что две конечные точки i-й линии находятся в (i, 0) и (i, height[i]).
# Найдите две линии, которые вместе с осью x образуют контейнер,
# такой что контейнер содержит максимальное количество воды.
# Верните максимальное количество воды, которое может храниться в контейнере.
#
# Task: "Container With Most Water"
# You are given an integer array height of length n. There are n vertical lines
# drawn such that the two endpoints of the ith line are
# (i, 0) and (i, height[i]).
# Find two lines that together with the x-axis form a container, such that
# the container contains the most water.
# Return the maximum amount of water a container can store.
#
# Example 1:
# Input: height = [1,8,6,2,5,4,8,3,7]
# Output: 49
# Explanation: The above vertical lines are represented by array
# [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section)
# the container can contain is 49.
#
# Example 2:
# Input: height = [1,1]
# Output: 1


from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        right, left = 0, len(height) - 1
        max_area = 0

        while right < left:
            max_area = max(
                max_area, ((left - right) * min(height[right], height[left]))
            )
            if height[right] < height[left]:
                right += 1
            else:
                left -= 1
        return max_area
