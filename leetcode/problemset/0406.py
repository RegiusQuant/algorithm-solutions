from typing import List


class Solution:

    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        people.sort(key=lambda x: (-x[0], x[1]))

        result = []
        for p in people:
            result[p[1]:p[1]] = [p]
        return result


if __name__ == "__main__":
    solution = Solution()
    print(solution.reconstructQueue([[7, 0], [4, 4], [7, 1], [5, 0], [6, 1], [5, 2]]))
    print(solution.reconstructQueue([[6, 0], [5, 0], [4, 0], [3, 2], [2, 2], [1, 4]]))
