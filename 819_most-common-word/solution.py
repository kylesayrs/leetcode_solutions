from typing import List


class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        banned = set(banned)

        words = []
        _word = ""
        for char in paragraph:
            if not char.isalpha() and len(_word) > 0:
                words.append(_word.lower())
                _word = ""
                
            elif char.isalpha():
                _word += char

        if len(_word) > 0:
            words.append(_word.lower())

        freq = defaultdict(lambda: 0)
        max_word = ""
        max_word_freq = 0
        for word in words:
            if word in banned: continue
            freq[word] += 1

            if freq[word] > max_word_freq:
                max_word = word
                max_word_freq = freq[word]

        return max_word
