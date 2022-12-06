from typing import List


class Solution:

    def checkPossibility(self, nums: List[int]) -> bool:
        if len(nums) <= 2:
            return True

        count = 0
        for i in range(len(nums) - 1):
            if nums[i] > nums[i + 1]:
                count += 1
                if i > 0 and nums[i + 1] < nums[i - 1]:
                    nums[i + 1] = nums[i]

        return count <= 1


if __name__ == "__main__":
    solution = Solution()
    print(solution.checkPossibility([4, 2, 3]))
    print(solution.checkPossibility([4, 2, 1]))
