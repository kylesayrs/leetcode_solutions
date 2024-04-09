from typing import List, Tuple


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        waiting: List[Tuple[int, int]] = []
        results = [0 for _ in range(len(temperatures))]

        for day, temperature in enumerate(temperatures):
            while len(waiting) > 0:
                prev_day, prev_temperature = waiting[-1]
                if prev_temperature >= temperature:
                    break

                results[prev_day] = day - prev_day
                waiting.pop()

            waiting.append((day, temperature))

        # days which are stuck on the waiting stack default to 0
        return results
                

if __name__ == "__main__":
    assert Solution().dailyTemperatures([73,74,75,71,69,72,76,73]) == [1,1,4,2,1,1,0,0]
    assert Solution().dailyTemperatures([30,40,50,60]) == [1,1,1,0]
    assert Solution().dailyTemperatures([30,60,90]) == [1,1,0]
    assert Solution().dailyTemperatures([5,4,3,2,1,3]) == [0, 0, 0, 2, 1, 0]
