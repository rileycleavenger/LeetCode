class Trie:

    def __init__(self):
        self.prefixes = set()
        self.dictionary = set()

    def insert(self, word: str) -> None:
        for i in range(len(word)):
            self.prefixes.add(word[:i+1])
        self.dictionary.add(word)

    def search(self, word: str) -> bool:
        return word in self.dictionary

    def startsWith(self, prefix: str) -> bool:
        return prefix in self.prefixes


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)