from typing import List


class Solution:
    def invert(self, val):
        if val == 0:
            return 1
        else:
            return 0

    def flipAndInvertImage(self, A: List[List[int]]) -> List[List[int]]:
        if len(A) > 0:
            lens = len(A[0])
        else:
            lens = 0
        for row_num, row in enumerate(A):
            start = 0
            end = lens - 1
            while ((start < end) and start != end):
                temp = self.invert(row[start])
                row[start] = self.invert(row[end])
                row[end] = temp
                start += 1
                end -= 1
            if end == start:
                row[start] = self.invert(row[start])
            A[row_num] = row
        return A


if __name__ == "__main__":
    sol = Solution()
    print(sol.flipAndInvertImage([[1, 1, 0], [1, 0, 1], [0, 0, 0]]))
    print(sol.flipAndInvertImage([[1, 1, 0, 0], [1, 0, 0, 1], [0, 1, 1, 1],
                                  [1, 0, 1, 0]]))
