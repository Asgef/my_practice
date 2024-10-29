# Task: Number of Islands
#
# Given a 2D binary grid 'grid' where '1' represents land and '0' represents
# water, return the number of islands.
#
# An island is surrounded by water and is formed by connecting adjacent lands
# horizontally or vertically. All four edges of the grid are
# surrounded by water.
#
#
# Задача: Количество Островов
#
# Дана 2D бинарная сетка 'grid', где '1' означает землю, а '0' — воду.
# Верните количество островов.
#
# Остров окружен водой и образован соединением смежных земель по горизонтали
# или вертикали. Все четыре края сетки окружены водой.
#
#
# Example 1:
# Input: grid = [
#   ["1","1","1","1","0"],
#   ["1","1","0","1","0"],
#   ["1","1","0","0","0"],
#   ["0","0","0","0","0"]
# ]
# Output: 1
#
# Example 2:
# Input: grid = [
#   ["1","1","0","0","0"],
#   ["1","1","0","0","0"],
#   ["0","0","1","0","0"],
#   ["0","0","0","1","1"]
# ]
# Output: 3


from typing import List
from collections import deque


class Solution: # noqa C901
    def numIslands(self, grid: List[List[str]]) -> int: # noqa C901

        def bfs(r, c):
            q = deque()
            q.append((r, c))
            visited.add((r, c))

            while q:
                row, col = q.popleft()

                direction = [[1, 0], [-1, 0], [0, 1], [0, -1]]
                for dr, dc, in direction:
                    r, c = dr + row, dc + col
                    if r in range(rows) and c in range(cols) and \
                            (r, c) not in visited and grid[r][c] == '1':
                        visited.add((r, c))
                        q.append((r, c))

        if not grid:
            return 0

        rows, cols = len(grid), len(grid[0])
        islands = 0
        visited = set()

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == '1' and (r, c) not in visited:
                    bfs(r, c)
                    islands += 1
        return islands

#  BFS, Обход в ширину
