from collections import defaultdict


class TrieNode:
    def __init__(self):
        self.children = defaultdict(TrieNode)
        self.isEnd = False


class Trie:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        currNode = self.root
        for char in word:
            currNode = currNode.children[char]
        currNode.isEnd = True

    def search(self, word: str) -> bool:
        currNode = self.root
        for char in word:
            currNode = currNode.children.get(char)
            if currNode is None:
                return False
        return currNode.isEnd

    def startsWith(self, prefix: str) -> bool:
        currNode = self.root
        for char in prefix:
            currNode = currNode.children.get(char)
            if currNode is None:
                return False
        return True


if __name__ == "__main__":
    test = Trie()
    test.insert("test")
    print(test.search("test"))
    print(test.startsWith("tes"))
