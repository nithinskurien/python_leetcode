class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        # Check if they have non-zero GCD string.
        if str1 + str2 != str2 + str1:
            return ""

        # Get the GCD of the two lengths.
        max_length = self.gcd(len(str1), len(str2))
        return str1[:max_length]

    def gcd(self, number1: int, number2: int) -> int:
        if number2 == 0:
            return number1
        else:
            return self.gcd(number2, number1 % number2)


if __name__ == '__main__':
    solution = Solution()
    print(solution.gcdOfStrings("ABCABC", "ABC"))
    print(solution.gcd(6, 4))
    print(solution.gcd(4, 6))
