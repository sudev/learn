from typing import List

c = 0


# Attempt one get's the count properly, calculates both half of the matrix though.
def longest_common_subsequence(seq1: List[str], seq2: List[str], cache):
    global c
    print(c)
    len1 = len(seq1)
    len2 = len(seq2)
    print("nope len1 = {} len2 = {}".format(len1, len2))
    if (len1 == 0) or (len2 == 0):
        return 0
    # Adjust for zero indexed array
    if cache[len1 - 1][len2 - 1] > 0:
        print("CACHED len1 = {} len2 = {}".format(len1, len2))
        return cache[len1 - 1][len2 - 1]
    val1 = seq1[-1]
    val2 = seq2[-1]
    if val1 == val2:
        val = 1 + longest_common_subsequence(seq1[:-1], seq2[:-1], cache)
    else:
        val = max(
            longest_common_subsequence(seq1[:-1], seq2, cache),
            longest_common_subsequence(seq1, seq2[:-1], cache))
    cache[len1 - 1][len2 - 1] = val
    c += 1
    return val


test_array_1 = ["A", "B", "C", "B", "D", "A", "B"]
test_array_2 = ["B", "D", "C", "A", "B", "A"]
print(
    longest_common_subsequence(test_array_1, test_array_2,
                               [[-1] * len(test_array_2)] * len(test_array_1)))
print(longest_common_subsequence(['A', 'B'], ['D'], [[-1] * 2] * 2))


def printer():
    print(test_array_1)


printer()