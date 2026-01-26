class Solution:
    def canCompleteCircuit(self, gas, cost):
        total_gas = 0
        tank = 0
        start = 0

        for i in range(len(gas)):
            diff = gas[i] - cost[i]
            total_gas += diff
            tank += diff

            if tank < 0:
                start = i + 1
                tank = 0

        return start if total_gas >= 0 else -1
