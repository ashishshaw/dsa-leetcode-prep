#Approach: O(n) -> For n gas stations
# 1. If total gas is less than total cost, return -1
# 2. Start from the first station and keep track of the gas in the tank
# 3. If at any point, the tank becomes negative, it means we cannot start from the previous station, so we reset the tank and move the start to the next station
# 4. If we can complete the circuit, return the start station

class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost):
            return -1

        start = 0
        tank = 0

        for i in range(len(gas)):
            tank += gas[i] - cost[i]
            if tank < 0:
                tank = 0
                start = i+1

        if tank >= 0:
            return start
        else:
            return -1
