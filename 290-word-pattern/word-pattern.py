class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        
        words = s.split(' ')
        
        if len(words) != len(pattern):
            return False
        
        wordToChar = {}
        charToWord = {}
        
        for w, c in zip(words, pattern):
            if w in wordToChar and wordToChar[w] != c:
                return False
            if c in charToWord and charToWord[c] != w:
                return False
            wordToChar[w] = c
            charToWord[c] = w
            
        return True