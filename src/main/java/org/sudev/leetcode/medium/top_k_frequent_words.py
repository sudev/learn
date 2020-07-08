import heapq
from typing import List
import heapq
from collections import Counter


class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        # Word repition counter
        counter = {}
        # for word in words:
        #     if word in counter:
        #         counter[word] = "{}_{}".format(
        #             int(counter[word].split("_")[0]) + 1, word)
        #     else:
        #         counter[word] = "{}_{}".format(1, word)
        # words = [x for x in counter.values()]
        count = Counter(words)
        heap = [(-val, key) for key, val in count.items()]
        heapq.heapify(heap)
        res = []
        while k > 0:
            res.append(heapq.heappop(heap)[1])
            k -= 1
        return res


if __name__ == "__main__":
    sol = Solution()
    print(sol.topKFrequent([
        "plpaboutit", "jnoqzdute", "sfvkdqf", "mjc", "nkpllqzjzp", "foqqenbey",
        "ssnanizsav", "nkpllqzjzp", "sfvkdqf", "isnjmy", "pnqsz", "hhqpvvt",
        "fvvdtpnzx", "jkqonvenhx", "cyxwlef", "hhqpvvt", "fvvdtpnzx",
        "plpaboutit", "sfvkdqf", "mjc", "fvvdtpnzx", "bwumsj", "foqqenbey",
        "isnjmy", "nkpllqzjzp", "hhqpvvt", "foqqenbey", "fvvdtpnzx", "bwumsj",
        "hhqpvvt", "fvvdtpnzx", "jkqonvenhx", "jnoqzdute", "foqqenbey",
        "jnoqzdute", "foqqenbey", "hhqpvvt", "ssnanizsav", "mjc", "foqqenbey",
        "bwumsj", "ssnanizsav", "fvvdtpnzx", "nkpllqzjzp", "jkqonvenhx",
        "hhqpvvt", "mjc", "isnjmy", "bwumsj", "pnqsz", "hhqpvvt", "nkpllqzjzp",
        "jnoqzdute", "pnqsz", "nkpllqzjzp", "jnoqzdute", "foqqenbey",
        "nkpllqzjzp", "hhqpvvt", "fvvdtpnzx", "plpaboutit", "jnoqzdute",
        "sfvkdqf", "fvvdtpnzx", "jkqonvenhx", "jnoqzdute", "nkpllqzjzp",
        "jnoqzdute", "fvvdtpnzx", "jkqonvenhx", "hhqpvvt", "isnjmy",
        "jkqonvenhx", "ssnanizsav", "jnoqzdute", "jkqonvenhx", "fvvdtpnzx",
        "hhqpvvt", "bwumsj", "nkpllqzjzp", "bwumsj", "jkqonvenhx", "jnoqzdute",
        "pnqsz", "foqqenbey", "sfvkdqf", "sfvkdqf"
    ], 1))
    print(sol.topKFrequent([
        "the", "day", "is", "sunny", "the", "the", "the", "sunny", "is", "is"
    ], 4))
    print(sol.topKFrequent(["the", "day", "the", "day"], 1))
    print(sol.topKFrequent(["i", "love", "leetcode", "i", "love", "coding"],
                           2))
