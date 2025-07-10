from collections import deque


class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        dire = deque()
        radiant = deque()
        length = len(senate)
        for index in range(length):
            if senate[index] == 'R':
                radiant.append(index)
            else:
                dire.append(index)
        while dire and radiant:
            popped_dire = dire.popleft()
            popped_radiant = radiant.popleft()
            if popped_radiant < popped_dire:
                radiant.append(popped_radiant + length)
            else:
                dire.append(popped_dire + length)
        return "Radiant" if radiant else "Dire"

if __name__ == "__main__":
    solution = Solution()
    print(solution.predictPartyVictory("RD"))
