from typing import List


# TODO - This is outputting wrong answer. Answer should have been 4, but outputs 3
# Memoisation - top - down
# Attempt one get's the count properly, calculates both half of the matrix though.
def longest_common_subsequence(seq1: List[str], seq2: List[str], cache):
    len1 = len(seq1)
    len2 = len(seq2)
    # print("nope len1 = {} len2 = {}".format(len1, len2))
    if (len1 == 0) or (len2 == 0):
        return 0
    # Adjust for zero indexed array
    if cache[len1 - 1][len2 - 1] > 0:
        # print("CACHED len1 = {} len2 = {}".format(len1, len2))
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
    return val


test_array_1 = ["A", "B", "C", "B", "D", "A", "B"]
test_array_2 = ["B", "D", "C", "A", "B", "A"]
print(
    longest_common_subsequence(test_array_1, test_array_2,
                               [[-1] * len(test_array_2)] * len(test_array_1)))
print(longest_common_subsequence(['A', 'B'], ['D'], [[-1] * 2] * 2))


# LCS - Dynamic
def lcs_dynamic(seq1: List[str], seq2: List[str]):
    temp = [[0] * (len(seq2) + 1)] * (len(seq1) + 1)
    maxi = 0
    for pos1 in range(0, len(seq1) + 1):
        for pos2 in range(0, len(seq2) + 1):
            if (pos1 == 0) or (pos2 == 0):
                val = 0
            elif seq1[pos1 - 1] == seq2[pos2 - 1]:
                val = 1 + temp[pos1 - 1][pos2 - 1]
            else:
                val = max(temp[pos1 - 1][pos2], temp[pos1][pos2 - 1])
            temp[pos1][pos2] = val
            print("Pos {} X {} => {}".format(pos1, pos2, val))
            if val > maxi:
                maxi = val
    return maxi


# GeeksforGeeks copied
def lcs(X, Y):
    # find the length of the strings
    m = len(X)
    n = len(Y)

    # declaring the array for storing the dp values
    L = [[None] * (n + 1) for i in range(m + 1)]
    """Following steps build L[m+1][n+1] in bottom up fashion 
    Note: L[i][j] contains length of LCS of X[0..i-1] 
    and Y[0..j-1]"""
    for i in range(m + 1):
        for j in range(n + 1):
            if i == 0 or j == 0:
                L[i][j] = 0
            elif X[i - 1] == Y[j - 1]:
                L[i][j] = L[i - 1][j - 1] + 1
            else:
                L[i][j] = max(L[i - 1][j], L[i][j - 1])
    # L[m][n] contains the length of LCS of X[0..n-1] & Y[0..m-1]
    return L[m][n]


print(lcs_dynamic(test_array_1, test_array_2))
print(lcs(test_array_1, test_array_2))