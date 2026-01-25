from collections import deque

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: list[str]) -> int:
        wordSet = set(wordList) # O(1) lookups
        if endWord not in wordSet:
            return 0
        
        # Queue stores (current_word, current_distance)
        queue = deque([(beginWord, 1)])
        
        while queue:
            word, length = queue.popleft()
            
            if word == endWord:
                return length
            
            # Try all possible 1-letter transformations
            for i in range(len(word)):
                original_char = word[i]
                for c in 'abcdefghijklmnopqrstuvwxyz':
                    if c == original_char:
                        continue
                        
                    next_word = word[:i] + c + word[i+1:]
                    
                    if next_word in wordSet:
                        queue.append((next_word, length + 1))
                        # Remove from set to avoid visiting the same word twice
                        wordSet.remove(next_word)
                        
        return 0