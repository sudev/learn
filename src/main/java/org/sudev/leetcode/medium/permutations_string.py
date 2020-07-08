class Solution:
    def check_completion(self, mas):
        for v in mas.values():
            if v != 0:
                return False
        return True

    # def reset_pos(self, mas):
    #     for k, v in mas.items():
    #         mas[k] = 0
    #     return mas
    def check_helper(self, s1, mas):
        for c in s1:
            if c in mas:
                if mas[c] == 0:
                    return False
                mas[c] = mas[c] - 1
            else:
                return False
        return True

    def checkInclusion(self, s1: str, s2: str) -> bool:
        # Setup
        mas = {}
        mas_default = {}
        for c in s1:
            if c in mas:
                mas[c] = mas[c] + 1
            else:
                mas[c] = 1
        len_s2 = len(s2)
        len_s1 = len(s1)
        for pos in range(len_s2):
            if (len_s2 - pos) < len_s1:
                return False
            if self.check_helper()


if __name__ == "__main__":
    sol = Solution()
    # print(sol.checkInclusion("ab", "eidbaooo"))
    # print(sol.checkInclusion("ab", "eidboaoo"))
    # print(sol.checkInclusion("adc", "dcda"))
    print(sol.checkInclusion("hello", "ooolleoooleh"))
