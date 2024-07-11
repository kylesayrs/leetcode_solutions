class Node:
    def __init__(self):
        self.is_end = False
        self.children = [None for _ in range(26)]

class Trie:

    def __init__(self):
        self.root = Node()
        self.zero = ord('a')

    def insert(self, word: str) -> None:
        current = self.root
        for character in word:
            char_index = ord(character) - self.zero
            if current.children[char_index] is None:
                current.children[char_index] = Node()

            current = current.children[char_index]

        current.is_end = True

    def search(self, word: str) -> bool:
        current = self.root
        for character in word:
            char_index = ord(character) - self.zero
            if current.children[char_index] is None:
                return False

            current = current.children[char_index]

        return current.is_end

    def startsWith(self, prefix: str) -> bool:
        current = self.root
        for character in prefix:
            char_index = ord(character) - self.zero
            if current.children[char_index] is None:
                return False

            current = current.children[char_index]

        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
