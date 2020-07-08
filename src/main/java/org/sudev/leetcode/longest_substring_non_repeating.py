from typing import Mapping


class Solution:
    def isValid(self, s: str) -> bool:
        temp = set()
        for c in s:
            if c in temp:
                return False
            temp.add(c)
        return True

    def recursion_with_some_memoisation(self, s: str,
                                        cache: Mapping[str, int]) -> int:
        if s in cache:
            return cache[s]
        if self.isValid(s):
            cache[s] = len(s)
            return cache[s]
        return max(
            self.recursion_with_some_memoisation(s[:-1], cache),
            self.recursion_with_some_memoisation(s[1:], cache))

    # It was very simple solution, had overcomplicated it using recusrion and backtracking in above function
    # This is copied from GfG after few bad attempts
    # Idea -- Window manipulation !!
    def longestUniqueSubsttr(self, string):
        # Creating a set to store the last positions of occurrence
        seen = {}
        maximum_length = 0
        # starting the inital point of window to index 0
        start = 0
        sub = ''
        for end in range(len(string)):
            # Checking if we have already seen the element or not
            if string[end] in seen:
                # If we have seen the number, move the start pointer
                # to position after the last occurrence
                start = max(start, seen[string[end]] + 1)
            # Updating the last seen value of the character
            seen[string[end]] = end
            if maximum_length < (end - start + 1):
                maximum_length = end - start + 1
                sub = string[start:end]
        print(sub)
        return maximum_length

    def lengthOfLongestSubstring(self, s: str) -> int:
        return self.longestUniqueSubsttr(s)


if __name__ == "__main__":
    sol = Solution()
    print(sol.lengthOfLongestSubstring("asdghhfgkjajshviualbdvkabygwbqw"))
