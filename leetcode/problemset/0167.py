from typing import List


class Solution:

    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        leftIndex, rightIndex = 0, len(numbers) - 1
        while leftIndex < rightIndex:
            currSum = numbers[leftIndex] + numbers[rightIndex]
            if currSum == target:
                return [leftIndex + 1, rightIndex + 1]
            if currSum < target:
                leftIndex += 1
            else:
                rightIndex -= 1
        return None


if __name__ == "__main__":
    solution = Solution()
    print(solution.twoSum([2, 7, 11, 15], 9))
    print(solution.twoSum([2, 3, 4], 6))
    print(solution.twoSum([-1, 0], -1))