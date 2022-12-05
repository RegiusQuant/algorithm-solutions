from typing import List


class Solution:

    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key=lambda x: x[1])

        result = 1
        rightBorder = points[0][1]
        for i in range(1, len(points)):
            if points[i][0] <= rightBorder:
                continue
            result += 1
            rightBorder = points[i][1]

        return result


if __name__ == "__main__":
    solution = Solution()
    print(solution.findMinArrowShots([[10, 16], [2, 8], [1, 6], [7, 12]]))
    print(solution.findMinArrowShots([[1, 2], [3, 4], [5, 6], [7, 8]]))
    print(solution.findMinArrowShots([[1, 2], [2, 3], [3, 4], [4, 5]]))
