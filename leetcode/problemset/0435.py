from typing import List


class Solution:

    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return 0

        intervals.sort(key=lambda x: x[1])

        result = 0
        rightBorder = intervals[0][1]
        for i in range(1, len(intervals)):
            if intervals[i][0] < rightBorder:
                result += 1
                continue
            rightBorder = intervals[i][1]

        return result


if __name__ == "__main__":
    solution = Solution()
    print(solution.eraseOverlapIntervals([[1, 2], [2, 3], [3, 4], [1, 3]]))
    print(solution.eraseOverlapIntervals([[1, 2], [1, 2], [1, 2]]))
    print(solution.eraseOverlapIntervals([[1, 2], [2, 3]]))
