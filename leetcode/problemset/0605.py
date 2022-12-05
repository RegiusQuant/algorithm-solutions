from typing import List


class Solution:

    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        count = 0

        for i in range(len(flowerbed)):
            if flowerbed[i] == 1:
                continue
            if i > 0 and flowerbed[i - 1] == 1:
                continue
            if i < len(flowerbed) - 1 and flowerbed[i + 1] == 1:
                continue
            count += 1
            flowerbed[i] = 1

        return count >= n


if __name__ == "__main__":
    solution = Solution()
    print(solution.canPlaceFlowers([1, 0, 0, 0, 1], 1))
    print(solution.canPlaceFlowers([1, 0, 0, 0, 1], 2))
