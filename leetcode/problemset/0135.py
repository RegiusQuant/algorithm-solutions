from typing import List


class Solution:

    def candy(self, ratings: List[int]) -> int:
        if not ratings:
            return 0

        nums = [1] * len(ratings)
        for i in range(1, len(ratings)):
            if ratings[i] > ratings[i - 1]:
                nums[i] = max(nums[i - 1] + 1, nums[i])
        for i in range(len(ratings) - 2, -1, -1):
            if ratings[i] > ratings[i + 1]:
                nums[i] = max(nums[i + 1] + 1, nums[i])

        return sum(nums)


if __name__ == "__main__":
    solution = Solution()
    print(solution.candy([1, 0, 2]))
    print(solution.candy([1, 2, 2]))
