class Solution:
    def asteroidCollision(self, asteroids: list[int]) -> list[int]:
        stack = []
        for asteroid in asteroids:
            while stack and stack[-1] > 0 > asteroid:
                popped_asteroid = stack.pop()
                if abs(popped_asteroid) > abs(asteroid):
                    stack.append(popped_asteroid)
                    break
                elif abs(popped_asteroid) == abs(asteroid):
                    break
            else:
                stack.append(asteroid)
        return stack

if __name__=="__main__":
    solution = Solution()
    print(solution.asteroidCollision([10,2,-5]))
    print(solution.asteroidCollision([5,10,-5]))
    print(solution.asteroidCollision([8,-8]))