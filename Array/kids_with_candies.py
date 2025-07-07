
class Solution:
    def kidsWithCandies(self, candies: list[int], extra_candies: int) -> list[bool]:
        bool_list = [False] * len(candies)
        max_candy = max(candies)
        for index in range(len(candies)):
            if candies[index] + extra_candies >= max_candy:
                bool_list[index] = True
        return bool_list
