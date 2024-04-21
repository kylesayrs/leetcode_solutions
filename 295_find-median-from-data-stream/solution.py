from typing import Optional, List

import heapq


def min_heap_pop(heap: List[int]) -> int:
    return heapq.heappop(heap)


def min_heap_push(heap: List[int], value: int):
    heapq.heappush(heap, value)


def min_heap_peek(heap: List[int]) -> int:
    return heap[0]


def max_heap_pop(heap: List[int]) -> int:
    return -heapq.heappop(heap)


def max_heap_push(heap: List[int], value: int):
    heapq.heappush(heap, -value)


def max_heap_peek(heap: List[int]) -> int:
    return -heap[0]


class MedianFinder:
    def __init__(self):
        self.left_heap = []
        self.right_heap = []
        self.median = None
        

    def addNum(self, num: int) -> None:
        # insert into heaps or median
        computed_median = self.findMedian()
        if computed_median is None:
            self.median = num
        
        elif num <= computed_median:
            max_heap_push(self.left_heap, num)

        else:
            min_heap_push(self.right_heap, num)

        # update median
        if len(self.left_heap) > len(self.right_heap):
            if self.median is None:
                self.median = max_heap_pop(self.left_heap)

            else:
                min_heap_push(self.right_heap, self.median)
                self.median = None

        if len(self.right_heap) > len(self.left_heap):
            if self.median is None:
                self.median = min_heap_pop(self.right_heap)

            else:
                max_heap_push(self.left_heap, self.median)
                self.median = None

        #print((self.left_heap, self.median, self.right_heap))
        assert len(self.left_heap) == len(self.right_heap)


    def findMedian(self) -> Optional[float]:
        if self.median is not None:
            return self.median
        
        assert len(self.left_heap) == len(self.right_heap)
        if len(self.left_heap) > 0:
            return (max_heap_peek(self.left_heap) + min_heap_peek(self.right_heap)) / 2
        
        return None


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()


if __name__ == "__main__":
    median_finder = MedianFinder()
    assert median_finder.findMedian() is None

    median_finder.addNum(5)
    assert median_finder.findMedian() == 5

    median_finder.addNum(6)
    assert median_finder.findMedian() == 5.5

    median_finder.addNum(4)
    assert median_finder.findMedian() == 5

    median_finder.addNum(5)
    assert median_finder.findMedian() == 5
