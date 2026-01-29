# 2976. Minimum Cost to Convert String I
#
# You are given two 0-indexed strings source and target, both of length n and consisting of lowercase English
# letters. You are also given two 0-indexed character arrays original and changed, and an integer array cost,
# where cost[i] represents the cost of changing the character original[i] to the character changed[i].
#
# You start with the string source. In one operation, you can pick a character x from the string and change it to the
# character y at a cost of z if there exists any index j such that cost[j] == z, original[j] == x, and changed[j] == y.
#
# Return the minimum cost to convert the string source to the string target using any number of operations. If it is
# impossible to convert source to target, return -1.
#
# Note that there may exist indices i, j such that original[j] == original[i] and changed[j] == changed[i].
#
#
#
# Example 1:
#
# Input: source = "abcd", target = "acbe", original = ["a","b","c","c","e","d"], changed = ["b","c","b","e","b","e"],
# cost = [2,5,5,1,2,20] Output: 28 Explanation: To convert the string "abcd" to string "acbe": - Change value at
# index 1 from 'b' to 'c' at a cost of 5. - Change value at index 2 from 'c' to 'e' at a cost of 1. - Change value at
# index 2 from 'e' to 'b' at a cost of 2. - Change value at index 3 from 'd' to 'e' at a cost of 20. The total cost
# incurred is 5 + 1 + 2 + 20 = 28. It can be shown that this is the minimum possible cost. Example 2:
#
# Input: source = "aaaa", target = "bbbb", original = ["a","c"], changed = ["c","b"], cost = [1,2] Output: 12
# Explanation: To change the character 'a' to 'b' change the character 'a' to 'c' at a cost of 1, followed by
# changing the character 'c' to 'b' at a cost of 2, for a total cost of 1 + 2 = 3. To change all occurrences of 'a'
# to 'b', a total cost of 3 * 4 = 12 is incurred. Example 3:
#
# Input: source = "abcd", target = "abce", original = ["a"], changed = ["e"], cost = [10000] Output: -1 Explanation:
# It is impossible to convert source to target because the value at index 3 cannot be changed from 'd' to 'e'.
#
#
# Constraints:
#
# 1 <= source.length == target.length <= 105
# source, target consist of lowercase English letters.
# 1 <= cost.length == original.length == changed.length <= 2000
# original[i], changed[i] are lowercase English letters.
# 1 <= cost[i] <= 106
# original[i] != changed[i]
#
# Logic:
# We can first create an adjacency list to know the neighbours to a node and the weight to travel there. We can
# then for each character create a minimum distance array indicating the dist to traverse the graph to reach all other
# characters including itself. We can calculate the minimum distance by using the dijkstra algorithm. We can do this for
# each character to make a matrix lookup. We can now go through the source and target indexes and use the lookup to add
# the cost to do the transformation.

import heapq
from collections import defaultdict


class Solution:
    def minimumCost(self, source: str, target: str, original: list[str], changed: list[str], cost: list[int]) -> int:
        adj = defaultdict(list)

        def change_char_to_index(char):
            return ord(char) - ord('a')

        for index in range(len(original)):
            adj[change_char_to_index(original[index])].append((cost[index], change_char_to_index(changed[index])))

        def dijkstra(source):
            dist = [float('inf')] * 26
            dist[source] = 0
            heap = [(0, source)]  # (weight, node)

            while heap:
                weight, node = heapq.heappop(heap)
                for new_weight, dest in adj[node]:
                    if weight + new_weight < dist[dest]:
                        dist[dest] = weight + new_weight
                        heapq.heappush(heap, (dist[dest], dest))
            return dist

        cost_array = [dijkstra(index) for index in range(26)]
        n = len(source)
        res = 0

        for index in range(n):
            scr, trg = change_char_to_index(source[index]), change_char_to_index(target[index])
            if cost_array[scr][trg] == float('inf'):
                return -1
            res += cost_array[scr][trg]

        return res



