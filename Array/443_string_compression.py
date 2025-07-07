class Solution:
    def compress(self, chars: list[str]) -> int:
        read_pointer, write_pointer, compressed_length, length = 0, 0, 0, len(chars)
        while read_pointer < length:
            next_read_pointer = read_pointer + 1
            while next_read_pointer < length and chars[next_read_pointer] == chars[read_pointer]:
                next_read_pointer += 1
            chars[write_pointer] = chars[read_pointer]
            write_pointer += 1
            if next_read_pointer - read_pointer > 1:
                total_group = str(next_read_pointer - read_pointer)
                for char in total_group:
                    chars[write_pointer] = char
                    write_pointer += 1
            read_pointer = next_read_pointer
        print(chars)
        return write_pointer

    def appendToResult(self, char: str, num: int, res: list):
        compressed_length_list = list(str(num))
        res.append(char)
        if num > 0:
            res.append(num)



if __name__ == "__main__":
    solution = Solution()
    print(solution.compress(["a","b","b","b","b","b","b","b","b","b","b","b","b"]))