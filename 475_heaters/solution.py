from typing import List

import math


class Solution:
    def findHousesMaxLeftRadius(houses: List[int], heaters: List[int]) -> List[int]:
        house_index = 0
        heater_index = 0
        house_left_radiuses = []

        # distance from house to left heater
        while house_index < len(houses):
            house_pos = houses[house_index]
            heater_pos = heaters[heater_index]
            next_heater_pos = heaters[heater_index + 1] if heater_index < len(heaters) - 1 else None

            # make sure house is to the right of heater
            if house_pos < heater_pos:
                house_left_radiuses.append(math.inf)
                house_index += 1
                continue

            # can move to a closer heater
            if next_heater_pos is not None and next_heater_pos <= houses[house_index]:
                heater_index += 1
                continue

            # update distance
            left_distance = house_pos - heater_pos
            house_left_radiuses.append(left_distance)

            # move house
            house_index += 1

        return house_left_radiuses
    

    def findHousesRightRadius(houses: List[int], heaters: List[int]) -> List[int]:
        houses = [-house_pos for house_pos in reversed(houses)]
        heaters = [-heater_pos for heater_pos in reversed(heaters)]

        return list(reversed(Solution.findHousesMaxLeftRadius(houses, heaters)))
        

    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        # sort
        houses.sort()
        heaters.sort()

        # distance from house to left heater
        house_left_radiuses = Solution.findHousesMaxLeftRadius(houses, heaters)

        # right to left
        house_right_radiuses = Solution.findHousesRightRadius(houses, heaters)

        #print(f"house_left_radiuses: {house_left_radiuses} house_right_radiuses: {house_right_radiuses}")
        
        # min each side, max each house
        return max([
            min(left, right)
            for left, right in zip(house_left_radiuses, house_right_radiuses)
        ])


if __name__ == "__main__":
    assert Solution().findRadius([1,2,3], [2]) == 1

    assert Solution().findRadius([1,2,3,100], [2]) == 98
    # assert Solution.findMaxLeftRadius([1,2,3,100], [2]) == 98
    # assert Solution.findRightRadius([1,2,3,100], [2]) == 1

    assert Solution().findRadius([1,2,3,4], [1, 4]) == 1
    # assert Solution.findMaxLeftRadius([1,2,3,4], [1, 4]) == 2
    # assert Solution.findRightRadius([1,2,3,4], [1, 4]) == 1

    assert Solution().findRadius([1,5], [2]) == 3

    # #Solution().findRadius([0,1,4,5,7], [2, 6])
