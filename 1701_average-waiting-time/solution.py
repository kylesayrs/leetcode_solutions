from typing import List

import math


class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
            #customers.sort(key=lambda x: x[0])

            total_wait_time = 0
            prev_order_end = -math.inf
            for customer_time, order_duration in customers:
                if customer_time < prev_order_end:
                    order_end = prev_order_end + order_duration
                else:
                    order_end = customer_time + order_duration

                total_wait_time += order_end - customer_time
                prev_order_end = order_end

            return total_wait_time / len(customers)
