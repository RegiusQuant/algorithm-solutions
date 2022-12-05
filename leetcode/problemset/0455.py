from typing import List


class Solution:

    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()

        gIndex = 0
        for i in range(len(s)):
            if gIndex >= len(g):
                break
            if s[i] >= g[gIndex]:
                gIndex += 1

        return gIndex


if __name__ == "__main__":
    solution = Solution()
    print(solution.findContentChildren([1, 2, 3], [1, 1]))
    print(solution.findContentChildren([1, 2], [1, 2, 3]))
