from typing import List


class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        num_questions = len(questions)
        cache = [None for _ in range(num_questions)]

        for index, (points, brain_power) in reversed(list(enumerate(questions))):
            cache[index] = max(
                (
                    cache[index + brain_power + 1]
                    if index + brain_power + 1 < num_questions
                    else 0
                ) + points,
                (
                    cache[index + 1]
                    if index + 1 < num_questions
                    else 0
                )
            )

        return cache[0]


if __name__ == "__main__":
    Solution().mostPoints([[1, 1]]) == 1
