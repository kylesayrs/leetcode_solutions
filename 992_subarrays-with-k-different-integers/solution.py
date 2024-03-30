from typing import List, Tuple, Dict

from collections import deque, defaultdict


class Solution:
    def subarraysWithKDistinct_eager(self, nums: List[int], k: int) -> int:
        right_most_index: Dict[int, int] = {}
        
        total_num_subarrays = 0
        left = 0
        for index, num in enumerate(nums):
            # get min right_most_index prior to adding
            min_key, min_index = (
                min(right_most_index.items(), key=lambda x: x[1])
                if len(right_most_index) > 0
                else (None, None)
            )
    
            # add right
            right_most_index[num] = index

            if len(right_most_index) < k:
                continue

            #if len(right_most_index) == k:
            #    pass

            if len(right_most_index) > k:
                # remove least right_most_index entry
                if min_key != num:
                    del right_most_index[min_key]

                left = min_index + 1

            if len(right_most_index) > 0:
                total_num_subarrays += 1 + (min(right_most_index.values()) - left)

            else:
                total_num_subarrays += 1
                            
        return total_num_subarrays
    

    # using near and far pointers is cool
    # I'm still a little unfamiliar with how freq relates to the max window
    # and the min window
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        freq: Dict[int, int] = defaultdict(lambda: 0)
        
        total_num_subarrays = 0
        left_far = 0
        left_near = 0
        for index, num in enumerate(nums):
            freq[num] += 1

            if len(freq) < k:
                continue

            # adjust max window
            adjusted_window = False
            while len(freq) > k:
                adjusted_window = True

                freq[nums[left_near]] -= 1
                if freq[nums[left_near]] <= 0:
                    del freq[nums[left_near]]

                left_near += 1
            
            if adjusted_window:
                left_far = left_near

            # adjust min window
            while freq[nums[left_near]] > 1:
                freq[nums[left_near]] -= 1
                left_near += 1

            total_num_subarrays += 1 + (left_near - left_far)

        return total_num_subarrays
            
            
if __name__ == "__main__":
    solution = Solution()

    #print(solution.subarraysWithKDistinct([1, 2, 1, 2, 3], 2))
    #print(solution.subarraysWithKDistinct([1, 2, 1, 3, 4], 3))
    print(solution.subarraysWithKDistinct([2, 1, 1, 1, 2], 1))
