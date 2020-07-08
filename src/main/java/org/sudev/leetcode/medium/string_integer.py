import re


class Solution:
    def myAtoi(self, str: str) -> int:
        mat = re.match("^\s*([+-]?)(\d+).*", str)
        if mat is None:
            return 0
        else:
            grps = mat.groups()
            val = int(grps[1])
            if grps[0] == "-":
                val = -1 * val
            if val > 2147483647:
                return 2147483647
            if val < -2147483648:
                return -2147483648
            return val


if __name__ == "__main__":
    sol = Solution()
    print(sol.myAtoi("-1213haodsfj"))
    print(sol.myAtoi("1213"))
    print(sol.myAtoi("   -0$%^&*("))
    print(sol.myAtoi("-1213haodsfj"))
    print(sol.myAtoi("+1213haodsfj"))
    print(sol.myAtoi("asd-1213haodsfj"))
    print(sol.myAtoi("a213haodsfj"))
