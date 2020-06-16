from typing import List


class Solution(object):
    # @param A : list of list of chars
    # @return nothing
    def solveSudoku(self, A):
        pass

    @staticmethod
    def clean_input(inp1: List[str]) -> List[int]:
        for pos, row in enumerate(inp):
            temp = []
            for elem in row:
                temp.append(elem)
            inp[pos] = temp
        return inp

    if __name__ == '__main__':
        inp = [["53..7...."], ["6..195..."], [".98....6."], ["8...6...3"],
               ["4..8.3..1"], ["7...2...6"], [".6....28."], ["...419..5"],
               ["....8..79"]]
        cleaned_input = Solution.clean_input(inp)
        print(cleaned_input)