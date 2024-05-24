from typing import List

class Solution:
    def maxScoreWords(self, words: List[str], letters: List[str], score: List[int]) -> int:
        num_words = len(words)
        word_scores = [
            sum(score[ord(char) - ord('a')] for char in word)
            for word in words
        ]
        freq = [0 for _ in range(26)]
        for letter in letters:
            freq[ord(letter) - ord('a')] += 1

        def subtract_word(freq: List[int], word_index: int) -> List[int]:
            nonlocal words

            freq_copy = freq.copy()
            for char in words[word_index]:
                freq_copy[ord(char) - ord('a')] -= 1

            return freq_copy
        

        def dfs(word_index: int, freq: List[int]) -> int:
            nonlocal word_scores
            nonlocal num_words
            
            if word_index >= num_words:
                return 0
            
            freq_without_word = subtract_word(freq, word_index)
            
            return max(
                word_scores[word_index] + dfs(word_index + 1, freq_without_word) if not any(f < 0 for f in freq_without_word) else 0,
                dfs(word_index + 1, freq)
            )
        
        return dfs(0, freq)


if __name__ == "__main__":
    assert Solution().maxScoreWords(
        ["dog","cat","dad","good"],
        ["a","a","c","d","d","d","g","o","o"],
        [1,0,9,5,0,0,3,0,0,0,0,0,0,0,2,0,0,0,0,0,0,0,0,0,0,0]
    ) == 23
