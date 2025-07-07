from collections import defaultdict


class Solution:
    def uniqueOccurrences(self, arr: list[int]) -> bool:
        output = defaultdict(int)
        for item in arr:
            output[item] += 1
        output_set = set(output.values())
        return len(output.values()) == len(output_set)
