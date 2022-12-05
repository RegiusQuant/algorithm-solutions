from typing import List


class Solution:

    def partitionLabels(self, s: str) -> List[int]:
        intervals = []
        for c in set(s):
            intervals.append((s.index(c), len(s) - s[::-1].index(c) - 1))

        intervals.sort(key=lambda x: x[0])

        result = []
        leftBorder, rightBorder = intervals[0][0], intervals[0][1]
        for i in range(1, len(intervals)):
            if intervals[i][0] < rightBorder:
                rightBorder = max(rightBorder, intervals[i][1])
            else:
                result.append(rightBorder - leftBorder + 1)
                leftBorder, rightBorder = intervals[i][0], intervals[i][1]
        result.append(rightBorder - leftBorder + 1)

        return result


if __name__ == "__main__":
    solution = Solution()
    print(solution.partitionLabels("ababcbacadefegdehijhklij"))
    print(solution.partitionLabels("eccbbbbdec"))
