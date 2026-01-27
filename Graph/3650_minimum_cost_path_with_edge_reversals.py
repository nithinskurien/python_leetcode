# 3650. Minimum Cost Path with Edge Reversals
#
# You are given a directed, weighted graph with n nodes labeled from 0 to n - 1, and an array edges where edges[i] =
# [ui, vi, wi] represents a directed edge from node ui to node vi with cost wi.
#
# Each node ui has a switch that can be used at most once: when you arrive at ui and have not yet used its switch,
# you may activate it on one of its incoming edges vi → ui reverse that edge to ui → vi and immediately traverse it.
#
# The reversal is only valid for that single move, and using a reversed edge costs 2 * wi.
#
# Return the minimum total cost to travel from node 0 to node n - 1. If it is not possible, return -1.
#
#
#
# Example 1:
#
# Input: n = 4, edges = [[0,1,3],[3,1,1],[2,3,4],[0,2,2]]
#
# Output: 5
#
# Explanation:
#
#
#
# Use the path 0 → 1 (cost 3).
# At node 1 reverse the original edge 3 → 1 into 1 → 3 and traverse it at cost 2 * 1 = 2.
# Total cost is 3 + 2 = 5.
# Example 2:
#
# Input: n = 4, edges = [[0,2,1],[2,1,1],[1,3,1],[2,3,3]]
#
# Output: 3
#
# Explanation:
#
# No reversal is needed. Take the path 0 → 2 (cost 1), then 2 → 1 (cost 1), then 1 → 3 (cost 1).
# Total cost is 1 + 1 + 1 = 3.
#
#
# Constraints:
#
# 2 <= n <= 5 * 104
# 1 <= edges.length <= 105
# edges[i] = [ui, vi, wi]
# 0 <= ui, vi <= n - 1
# 1 <= wi <= 1000
#
# Logic: This code implements Dijkstra's algorithm to find the shortest path in a weighted graph, but with an
# interesting twist: the graph is directional with asymmetric costs. Key Insight The most important part is this
# section:
# src, dest, weight in edges:
#   adj[src].append((dest, weight))
#   adj[dest].append((src, 2 * weight))
# This creates a graph where:
#
# Going from src → dest costs weight
# Going from dest → src costs 2 * weight (double!)
#
# So edges have different costs depending on which direction you traverse them.
# How It Works
# Initialization:
#
# dist[0] = 0 (starting node has distance 0)
# All other nodes have distance infinity
# Min-heap starts with node 0
#
# Main Loop:
# The algorithm explores nodes in order of their shortest known distance:
#
# Pop the node with minimum distance from the heap
# Skip stale entries - if we've already found a better path to this node, ignore this entry
# Early exit - if we reach the target node (n-1), return immediately
# Relax edges - for each neighbor, if we found a shorter path, update its distance and add it to the heap

import heapq
from collections import defaultdict


class Solution:
    def minCost(self, n: int, edges: list[list[int]]) -> int:
        adj = defaultdict(list)
        dist = [0] + [float('inf')] * (n - 1)
        heap = []
        heapq.heappush(heap, (0, 0))  # w, neighbour

        for src, dest, weight in edges:
            adj[src].append((dest, weight))
            adj[dest].append((src, 2 * weight))

        while heap:
            weight, node = heapq.heappop(heap)

            # stale entry
            if weight > dist[node]:
                continue

            # early exit
            if node == n - 1:
                return weight

            for neighbour, neighbour_weight in adj[node]:
                if weight + neighbour_weight < dist[neighbour]:
                    dist[neighbour] = weight + neighbour_weight
                    heapq.heappush(heap, (dist[neighbour], neighbour))

        return dist[n - 1] if dist[n - 1] != float('inf') else -1
