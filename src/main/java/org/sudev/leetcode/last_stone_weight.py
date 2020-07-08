import heapq
from typing import List


class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # negate stone weights so we can use heapq module (which provides a min-heap)
        stones = [w for w in stones]
        heapq.heapify(stones)  # O(n)
        while len(stones) > 1:
            # get two heaviest stones
            w1 = heapq.heappop(stones)  # heavier (more negative)
            w2 = heapq.heappop(stones)  # lighter (less negative)
            if w1 != w2:
                heapq.heappush(stones, w1 - w2)
        if (len(stones) > 0):
            return -stones[0]
        else:
            return 0


if __name__ == "__main__":
    sol = Solution()
    print(sol.lastStoneWeight([2, 7, 4, 1, 8, 1]))
    print(sol.lastStoneWeight([2, 2]))
    # 10, 10, 8, 7, 5, 4, 3, 1
    print(sol.lastStoneWeight([10, 5, 4, 10, 3, 1, 7, 8]))
    print(sol.lastStoneWeight(["1_A", "4_D", "2_B"]))
