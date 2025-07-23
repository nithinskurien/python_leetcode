from __future__ import annotations

from collections import defaultdict


class TrieNode:
    def __init__(self):
        self.children = defaultdict(TrieNode)
        self.product = []


class Trie:

    def __init__(self):
        self.root = TrieNode()
        self.returnCount = 3

    def insert(self, word: str) -> None:
        currNode = self.root
        self.addProduct(currNode, word)
        for char in word:
            currNode = currNode.children[char]
            self.addProduct(currNode, word)

    def search(self, word: str) -> list[str]:
        currNode = self.root
        for char in word:
            currNode = currNode.children.get(char)
            if currNode is None:
                return []
        return currNode.product

    def addProduct(self, node: TrieNode, word: str) -> None:
        if len(node.product) < self.returnCount:
            node.product.append(word)


class Solution:
    def suggestedProducts(self, products: list[str], searchWord: str) -> list[list[str]]:
        products.sort()
        trie = Trie()
        for product in products:
            trie.insert(product)
        result = []
        search = ""
        for char in searchWord:
            search += char
            result.append(trie.search(search))
        return result


if __name__ == "__main__":
    print(Solution().suggestedProducts(["mobile", "mouse", "moneypot", "monitor", "mousepad"], "mouse"))
