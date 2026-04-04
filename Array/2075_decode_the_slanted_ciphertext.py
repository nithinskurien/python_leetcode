# 2075. Decode the Slanted Ciphertext
#
# A string originalText is encoded using a slanted transposition cipher to a string encodedText with the help of a
# matrix having a fixed number of rows rows.
#
# originalText is placed first in a top-left to bottom-right manner.
#
#
# The blue cells are filled first, followed by the red cells, then the yellow cells, and so on, until we reach the
# end of originalText. The arrow indicates the order in which the cells are filled. All empty cells are filled with '
# '. The number of columns is chosen such that the rightmost column will not be empty after filling in originalText.
#
# encodedText is then formed by appending all characters of the matrix in a row-wise fashion.
#
#
# The characters in the blue cells are appended first to encodedText, then the red cells, and so on, and finally the
# yellow cells. The arrow indicates the order in which the cells are accessed.
#
# For example, if originalText = "cipher" and rows = 3, then we encode it in the following manner:
#
#
# The blue arrows depict how originalText is placed in the matrix, and the red arrows denote the order in which
# encodedText is formed. In the above example, encodedText = "ch ie pr".
#
# Given the encoded string encodedText and number of rows rows, return the original string originalText.
#
# Note: originalText does not have any trailing spaces ' '. The test cases are generated such that there is only one
# possible originalText.
#
#
#
# Example 1:
#
# Input: encodedText = "ch   ie   pr", rows = 3
# Output: "cipher"
# Explanation: This is the same example described in the problem description.
# Example 2:
#
#
# Input: encodedText = "iveo    eed   l te   olc", rows = 4
# Output: "i love leetcode"
# Explanation: The figure above denotes the matrix that was used to encode originalText.
# The blue arrows show how we can find originalText from encodedText.
# Example 3:
#
#
# Input: encodedText = "coding", rows = 1
# Output: "coding"
# Explanation: Since there is only 1 row, both originalText and encodedText are the same.
#
#
# Constraints:
#
# 0 <= encodedText.length <= 106
# encodedText consists of lowercase English letters and ' ' only.
# encodedText is a valid encoding of some originalText that does not have trailing spaces.
# 1 <= rows <= 1000
# The testcases are generated such that there is only one possible originalText.
#
# Logic:
# 🧠 Big Idea
#
# The string encoded_text was originally written into a grid with a fixed number of rows, then read diagonally (
# top-left → bottom-right) to produce the encoded string.
#
# This function reverses that process to recover the original message.
#
# 📦 Step 1: Handle simple case
# if rows == 1:
#     return encoded_text
#
# If there’s only one row, nothing was rearranged — just return the text.
#
# 📏 Step 2: Reconstruct the grid shape
# N = len(encoded_text)
# cols = N // rows
# N: total characters
# cols: number of columns in the grid
#
# So the original text was placed in a grid like:
#
# rows × cols
# 🔁 Step 3: Traverse diagonally
#
# This is the core logic:
#
# i, j, k = 0, 0, 0
# original_text = []
# i = row index
# j = column index
# k = index in the string
# 🔄 The loop
# while k < N:
#     original_text.append(encoded_text[k])
#
# We pick characters from encoded_text in a special pattern.
#
# 📉 Move diagonally
# i += 1
#
# Move down one row.
#
# 🔁 Reset when hitting bottom
# if i == rows:
#     i = 0
#     j += 1
#
# If we go past the last row:
#
# jump back to top row
# move one column to the right
# 🧮 Compute next index
# k = i*(cols + 1) + j
#
# This is the trickiest part.
#
# It calculates the position in the string that corresponds to moving diagonally in the grid.
#
# Why (cols + 1)?
#
# Moving diagonally means:
# go 1 row down
# go 1 column right
# In a flattened grid, that equals jumping cols + 1 steps
#
# So:
#
# index = row * (cols + 1) + column
# ✂️ Step 4: Clean up result
# return ''.join(original_text).rstrip()
# Join characters into a string
# Remove trailing spaces (important — padding may exist)
#

class Solution:
    def decodeCiphertext(self, encoded_text: str, rows: int) -> str:
        if rows == 1:
            return encoded_text

        N = len(encoded_text)
        cols = N // rows
        i, j, k = 0, 0, 0
        original_text = []

        while k < N:
            original_text.append(encoded_text[k])
            i += 1
            if i == rows:
                i = 0
                j += 1
            k = i*(cols + 1) + j

        return ''.join(original_text).rstrip()
