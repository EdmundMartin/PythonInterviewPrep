from typing import List


class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        start_cords = None
        for row in range(len(grid)):
            for col in range(len(grid[row])):
                if grid[row][col] == 1:
                    start_cords = (row, col)
                    break
        seen = set()
        seen.add(start_cords)
        island_perimeter = 0
        queue = [start_cords]
        while queue:
            cords = queue.pop(0)
            neighbors = self.neighbors(grid, cords)
            island_perimeter += 4 - len(neighbors)
            for neighbor in neighbors:
                if neighbor not in seen:
                    queue.append(neighbor)
                    seen.add(neighbor)
        return island_perimeter

    def neighbors(self, grid, cords):
        row, col = cords
        neighbors = []
        if row + 1 < len(grid) and grid[row + 1][col] == 1:
            neighbors.append((row + 1, col))
        if row - 1 >= 0 and grid[row - 1][col] == 1:
            neighbors.append((row - 1, col))
        if col + 1 < len(grid[row]) and grid[row][col + 1] == 1:
            neighbors.append((row, col + 1))
        if col - 1 >= 0 and grid[row][col - 1] == 1:
            neighbors.append((row, col - 1))
        return neighbors


if __name__ == '__main__':
    grid = [[0, 1, 0, 0], [1, 1, 1, 0], [0, 1, 0, 0], [1, 1, 0, 0]]

    result = Solution().islandPerimeter(grid)
    print(result)